--
-- 由SQLiteStudio v3.2.1 产生的文件 周三 6月 3 12:27:15 2020
--
-- 文本编码：System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- 表：book
DROP TABLE IF EXISTS book;
CREATE TABLE book (id INTEGER PRIMARY KEY, picture TEXT, owner REFERENCES user (id), price REAL, discount REAL, amount INTEGER);

-- 表：comment
DROP TABLE IF EXISTS comment;
CREATE TABLE comment (id INTEGER PRIMARY KEY, bookId REFERENCES book (id), userId REFERENCES user (id), content TEXT, created TIMESTAMP DEFAULT (CURRENT_TIMESTAMP));

-- 表：user
DROP TABLE IF EXISTS user;
CREATE TABLE user (id INTEGER PRIMARY KEY, sex TEXT, username TEXT UNIQUE, password TEXT);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
