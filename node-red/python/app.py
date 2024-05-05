import nicegui
import sqlite3

from nicegui import ui

from starlette.responses import JSONResponse

from typing import List

DATABASE = "database.db"

# 连接到数据库并返回db对象
def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db


# 初始化数据库
def init_db():
    with get_db() as db:
        cur = db.cursor()
        exists = cur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='users'").fetchone()[0]
        if exists == 0:
            with open('schema.sql', mode='r') as f:
                cur.executescript(f.read())
            db.commit()


# 获取所有用户
def fetch_users():
    with get_db() as db:
        cur = db.cursor()
        cur.execute("SELECT name FROM users")
        return [row['name'] for row in cur.fetchall()]


class Users:
    def __init__(self):
        self.userList = fetch_users()
        self.currentUser = self.userList[0]

    def update(self):
        self.userList = fetch_users()

    def set_current_user(self, username: str):
        assert username in self.userList
        self.currentUser = username

    def register_user(self, username):
        if username:
            with get_db() as db:
                cur = db.cursor()
                cur.execute("INSERT INTO users (name) VALUES (?)", (username,))
                db.commit()
            self.update()

    def delete_user(self, username):
        with get_db() as db:
            cur = db.cursor()
            cur.execute("DELETE FROM users WHERE name=?", (username,))
            db.commit()
        self.update()


def user_change(e, users_instance: Users, stock_link_instance: ui.link):
    users_instance.set_current_user(e.value)
    stock_link_instance.target = '/{}/stock'.format(e.value)
    stock_link_instance.update()


def user_add_callback(ui_selection: List[ui.select], users_instance: Users, value):
    ui.notify('User Added')
    users_instance.register_user(value)
    users_instance.update()
    for box in ui_selection:
        box.options = users_instance.userList
        box.value = users.currentUser
        box.update()


def user_delete_callback(ui_selection: List[ui.select], users_instance: Users, value):
    ui.notify('User Deleted')
    users_instance.delete_user(value)
    users_instance.update()
    for box in ui_selection:
        box.options = users_instance.userList
        box.value = users.currentUser
        box.update()


def fetch_inventory_by_username(username: str):
    with get_db() as db:
        cur = db.cursor()
        # 执行参数化查询，避免SQL注入
        cur.execute("SELECT * FROM inventories WHERE user_name = ?", (username,))
        results = cur.fetchall()

        # 将结果转换为字典列表，除去 user_name 键
        inventory_list = []
        for row in results:
            # 转换 Row 为 dict
            d = dict(row)
            del d['id']
            del d['user_name']
            inventory_list.append(d)

        return inventory_list


@ui.page('/')
def index():
    with ui.card():
        ui.markdown("# User Management")

        with ui.card():
            ui.markdown("## User Selection")
            userSelect = ui.select(options=users.userList,
                                   value=users.currentUser,
                                   on_change=lambda e: user_change(
                                       e,
                                       users_instance=users,
                                       stock_link_instance=gotoStock))

        with ui.card():
            ui.markdown("## User Unregister")
            userDelete = ui.select(options=users.userList, value=users.currentUser)
            ui.button("Delete", on_click=lambda: user_delete_callback(
                ui_selection=[userSelect, userDelete],
                users_instance=users,
                value=userDelete.value
            ))

        with ui.card():
            ui.markdown("## User Register")
            userAdd = ui.input("User Register", placeholder="Your user name")
            ui.button("Submit", on_click=lambda: user_add_callback(
                ui_selection=[userSelect, userDelete],
                users_instance=users,
                value=userAdd.value
            ))
    gotoStock = ui.link('GO TO MY STOCK', target='/{}/stock'.format(users.currentUser))


@ui.page('/{username}/stock')
def stock(username: str):
    with ui.card():
        ui.markdown("# Hi {}, here is your stock".format(username))

    inventList = fetch_inventory_by_username(username)
    grid = ui.aggrid({
        'defaultColDef': {'flex': 1},
        'columnDefs': [
            {'headerName': 'Food', 'field': 'food_name'},
            {'headerName': 'Type', 'field': 'type'},
            {'headerName': 'Quantity', 'field': 'quantity'},
            {'headerName': 'Expiration Date', 'field': 'expiration'},
        ],
        'rowData': inventList,
        'rowSelection': 'multiple',
    }).classes('max-h-40')

    def update_stock():
        grid.options['rowData'] = fetch_inventory_by_username(username)
        grid.update()

    ui.button('Update', on_click=update_stock)

    ui.link("BACK TO USER PAGE", target='/')


@ui.page('/debug')
def debug():
    return JSONResponse({"message": "Hello developer!", "status": 200})

init_db()
users = Users()
ui.run()