CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    bio TEXT,
    email TEXT UNIQUE,
    password TEXT
);

CREATE TABLE follows (
    username TEXT,
    following TEXT,
    FOREIGN KEY (username, following) REFERENCES users (username, username),
    PRIMARY KEY (username, following)
);

INSERT INTO users (username, bio, email,password) VALUES("reindeer",
"I think I will buy the red car",
"reindeerblazarpiepie@gmail.com",
"reindeer"
);

INSERT INTO users (username, bio, email,password) VALUES("star-lord",
"She wondered what his eyes were saying",
"star-lord@gmail.com",
"star-lord"
);

INSERT INTO users (username, bio, email,password) VALUES("rye",
"The stench from the feedlot",
"rye@gmail.com",
"rye"
);

INSERT INTO users (username, bio, email,password) VALUES("thegreenmile",
"She wondered what his eyes were saying",
"thegreenmile@gmail.com",
"thegreenmile"
);

INSERT INTO users (username, bio, email,password) VALUES("lastrada",
"In hopes of finding out the truth",
"lastrada@gmail.com",
"lastrada"
);

INSERT INTO users (username, bio, email,password) VALUES("kyanite",
"Entered the one-room library",
"kyanite@gmail.com",
"kyanite"
);

INSERT INTO users (username, bio, email,password) VALUES("thedeparted",
"All you need to do is pick up the pen and begin.",
"thedeparted@gmail.com",
"thedeparted"
);

INSERT INTO users (username, bio, email,password) VALUES("petrichor",
"Nobody loves a pig wearing lipstick.",
"petrichor@gmail.com",
"petrichor"
);

INSERT INTO follows (username, following) VALUES ("kyanite", "lastrada");
INSERT INTO follows (username, following) VALUES ("lastrada", "kyanite");
INSERT INTO follows (username, following) VALUES ("lastrada", "thegreenmile");
INSERT INTO follows (username, following) VALUES ("rye", "reindeer");
INSERT INTO follows (username, following) VALUES ("thedeparted", "star-lord");
INSERT INTO follows (username, following) VALUES ("reindeer", "star-lord");
INSERT INTO follows (username, following) VALUES ("star-lord", "reindeer");