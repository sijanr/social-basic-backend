import configparser
import logging.config

import hug
import sqlite_utils

#Load configuration
config = configparser.ConfigParser()
config.read("./etc/api.ini")
logging.config.fileConfig(config["logging"]["config"], disable_existing_loggers= False)

@hug.directive()
def usersdb(section="sqlite", key="usersdb", **kwargs):
    dbfile = config[section][key]
    return sqlite_utils.Database(dbfile)

@hug.authentication.basic
@hug.get("/verifyUser")
def isUserInTheDatabase(username, password, hug_usersdb):
    print("Username is ", str(username))
    print("Password is ", str(password))
    db = usersdb()
    result = db.query("SELECT * FROM users WHERE username==\"{}\" AND password==\"{}\"".format(str(username), str(password)))
    for row in result:
        return True
    return False

@hug.post("/signup/", status = hug.falcon.HTTP_201)
def createUser(
    response,
    username: hug.types.text,
    bio: hug.types.text,
    email: hug.types.text,
    password: hug.types.text,
    hug_usersdb
):
    users = hug_usersdb["users"]
    user = {
        "username": username,
        "bio": bio,
        "email": email,
        "password": password,
    }
    try:
        users.insert(user)
    except Exception as e:
        response.status = hug.falcon.HTTP_409
        return {"success":"false","error":str(e)}
    return {"success": "true"}


@hug.get("/get_following")
def getUserFollowing(username: hug.types.text, hug_usersdb):
    db = hug_usersdb
    result = db.query("SELECT following FROM follows WHERE username==\"{}\"".format(str(username)))
    list = []
    for row in result:
        list.append(row)
    return list

@hug.post("/follow", status=hug.falcon.HTTP_201, requires=isUserInTheDatabase)
def followUser(response, yourUsername: hug.types.text, followingUsername: hug.types.text, hug_usersdb):
    followingdb = hug_usersdb["follows"]
    user = {
        "username": yourUsername,
        "following": followingUsername
    }
    try:
        followingdb.insert(user)
    except Exception as e:
        response.status = hug.falcon.HTTP_409
        return {"success": "false", "error": str(e)}
    return {"success":"true"}



hug.API(__name__).http.serve(port=8001)