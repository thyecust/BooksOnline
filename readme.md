# BooksOnline

ECUST *Programming Practice 2020 Spring* Final Project.

## Grading Requirements

1. ~~"商品显示"界面添加各商品的"查看商品详情"链接，展示每件商品的所有信息~~
2. ~~"商品显示"界面中商品数至少 12 件，分页显示，每页显示 5 件商品~~
3. ~~在"用户登录"界面添加"验证码"的输入文本框，验证码是随机生成的~~
4. ~~"用户注册"界面添加性别的输入~~
5. ~~"商品显示"界面显示"欢迎\*\*先生光临"或"欢迎\*\*女士"光临~~
6. ~~将网站修改为你喜欢销售的实体或虚拟商品~~
7. ~~将"关于我们"界面内容修改为学号+姓名~~
8. 商品会员价的计算方式更改为 *会员价=单价\*折扣*
9. 购物成功界面添加到"工行""农行"等银行在线支付界面的链接
10. 购物车界面在总计中添加折扣总计，即用户享受的折扣总和
11. ~~进入购物车界面，每项物品前有勾选框，选定物品后进入订单确认，显示商品图片、名称、单价、简介信息、购买数量，订单确认后进入支付页面~~

Grades：

1. 完成 1-10，根据完成情况评分在 70-85
2. 完成 1-11，根据完成情况评分在 85-90
3. 完成更多功能，根据情况评分在 90-100

## Solutions

This project is constructed by Flask, a simple Python Web Framework.

Database is constructed by SQLite3, since Python has `sqlite3` lib.

Pagination is implemented by `SELCET * FROM table LIMIT 5 OFFSET n`, where `n` starts at `0`.

## Development

See [Development](./docs/development.md)

## Thanks

This course is instructed by **Zhai(May)**. Thanks her.

Thanks my group partner,

* **Sun(Sixon)**
* **Wang**
* **Li**
* **Zhang**
* **Han**