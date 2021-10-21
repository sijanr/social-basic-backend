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

@hug.directive()
def postsdb(section="sqlite", key="postsdb", **kwargs):
    dbfile = config[section][key]
    return sqlite_utils.Database(dbfile)

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
        return {"error":str(e)}
    return user



