import configparser
import logging.config
from base64 import b64encode

import hug
import sqlite_utils
import requests
import datetime

#Load configuration
config = configparser.ConfigParser()
config.read("./etc/api.ini")
logging.config.fileConfig(config["logging"]["config"], disable_existing_loggers= False)

@hug.directive()
def postsdb(section="sqlite", key="postsdb", **kwargs):
    dbfile = config[section][key]
    return sqlite_utils.Database(dbfile)

@hug.authentication.basic
def checkUserAuthorization(username, password):
    print(username)
    print(password)
    r = requests.get("http://localhost:8001/verifyUser", data={"username":str(username),"password":str(password)})
    print(r.text)
    if "true" in r.text:
        return True
    else:
        return False

@hug.get("/home_timeline", requires=checkUserAuthorization)
def getHomeTimeline(username:hug.types.text, hug_postsdb):
    r = requests.get("http://localhost:8001/get_following", data={"username":str(username)})
    followingJSON = r.json()
    string = ""
    for following in followingJSON:
        string += "\"" + following["following"] + "\"" + " OR username="
    if len(string) > 0:
        queryString = "SELECT * FROM posts WHERE username=" + string.strip()[0:len(string)-13].strip() + " ORDER BY timestamp DESC"
        result = hug_postsdb.query(queryString)
        list = []
        for row in result:
            list.append(row)
        return list
    return []


@hug.get("/user_timeline", requires=checkUserAuthorization)
def getUserTimeline(username: hug.types.text, hug_postsdb):
    db = hug_postsdb
    result = db.query("SELECT * FROM posts WHERE username==\"{}\" ORDER BY timestamp DESC".format(str(username)))
    list = []
    for row in result:
        print(row)
        list.append(row)
    return list

@hug.get("/public_timeline")
def getPublicTimeline(hug_postsdb):
    result = hug_postsdb.query("SELECT * FROM posts ORDER BY timestamp DESC")
    list = []
    for row in result:
        list.append(row)
    return list

@hug.post("/create_post", requires=checkUserAuthorization)
def createPost(username: hug.types.text, post_text: hug.types.text, hug_postsdb, response, **kwargs):
    db = hug_postsdb["posts"]
    date = datetime.datetime.now()
    timeStamp = str(date)[0:19]
    post = {
        "username": username,
        "post": post_text,
        "timestamp": timeStamp
    }
    if (kwargs["repost"]):
        post["repost"] = "/posts/{}".format(kwargs["repost"])
    try:
        db.insert(post)
    except Exception as e:
        response.status = hug.falcon.HTTP_409
        return {"error":str(e)}
    return {"status":"success"}

@hug.get("/posts/{id}")
def getPost(response, id: hug.types.number, hug_postsdb):
    posts = []
    try:
        post = hug_postsdb["posts"].get(id)
        posts.append(post)
    except sqlite_utils.db.NotFoundError:
        response.status = hug.falcon.HTTP_404
    return {"post": posts}