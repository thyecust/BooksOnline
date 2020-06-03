# 开发过程

## 数据库设计

设计了三个数据表，`user`，`book`，`comment`，如下

```sql
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
```

第一次提交。

## 视图

BooksOnline 设计了 3 个视图：

* `auth`，用于验证账号身份
* `explore`，用于发布商品、浏览商品、加入购物车
* `check`，用于购物车结算

`auth` 包含两个页面

* `login.html`，登录
* `register.html`，注册，完成了目标4

第二次提交。