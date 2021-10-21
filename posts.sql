PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS posts(
    username TEXT,
    post TEXT,
    timestamp TEXT,
    repost TEXT,
    PRIMARY KEY (username, timestamp)
);

INSERT INTO posts (username, post, timestamp) VALUES(
    "reindeer",
    "I think I will buy the red car, or I will lease the blue one.",
    "1923-09-23 14:23:24"
);

INSERT INTO posts (username, post, timestamp) VALUES(
    "star-lord",
    "There was coal in his stocking and he was thrilled.",
    "1934-05-08 00:23:18"
);

INSERT INTO posts (username, post, timestamp) VALUES(
    "rye",
    "The busker hoped that the people passing by would throw money, but they threw tomatoes instead, so he exchanged his hat for a juicer.",
    "1945-08-11 08:45:54"
);

INSERT INTO posts (username, post, timestamp) VALUES(
    "thegreenmile",
    "There was coal in his stocking and he was thrilled.",
    "2000-07-28 02:09:32"
);

INSERT INTO posts (username, post, timestamp) VALUES(
    "reindeer",
    "We need to rent a room for our party.",
    "1923-09-24 09:27:43"
);

INSERT INTO posts (username, post, timestamp) VALUES(
    "thegreenmile",
    "She thought there'd be sufficient time if she hid her watch.",
    "1923-09-23 10:10:26"
);

INSERT INTO posts (username, post, timestamp) VALUES(
    "rye",
    "The bug was having an excellent day until he hit the windshield.",
    "1983-01-23 18:05:13"
);

INSERT INTO posts (username, post, timestamp) VALUES(
    "petrichor",
    "Homesickness became contagious in the young campers' cabin.",
    "1948-04-13 23:35:45"
);

INSERT INTO posts (username, post, timestamp) VALUES(
    "thedeparted",
    "A kangaroo is really just a rabbit on steroids.",
    "1998-06-07 22:30:43"
);