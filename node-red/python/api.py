from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'database.db'


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/api/test', methods=['POST'])
def submit():
    data = request.json
    return jsonify({'received': data, 'status': 'success'})


@app.route('/api/invent-in', methods=['POST'])
def invent_in():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM inventories WHERE food_name = ? AND type = ? AND expiration = ?',
                   (data['name'], data['type'], data['expiration']))
    inventory = cursor.fetchone()
    if inventory:
        # 如果食物已存在，则增加数量
        new_quantity = inventory['quantity'] + 1
        cursor.execute('UPDATE inventories SET quantity = ? WHERE id = ?',
                       (new_quantity, inventory['id']))
    else:
        # 如果食物不存在，则添加新的食物条目
        cursor.execute(
            'INSERT INTO inventories (user_name, food_name, type, quantity, expiration) VALUES (?, ?, ?, ?, ?)',
            ('DEFAULT', data['name'], data['type'], 1, data['expiration']))
    conn.commit()
    conn.close()
    return jsonify({'received': data, 'status': 'success'})


@app.route('/api/invent-out', methods=['POST'])
def invent_out():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM inventories WHERE food_name = ? AND type = ? AND expiration = ?',
                   (data['name'], data['type'], data['expiration']))
    inventory = cursor.fetchone()
    if inventory:
        new_quantity = inventory['quantity'] - 1
        if new_quantity > 0:
            cursor.execute('UPDATE inventories SET quantity = ? WHERE id = ?',
                           (new_quantity, inventory['id']))
        else:
            cursor.execute('DELETE FROM inventories WHERE id = ?', (inventory['id'],))
    conn.commit()
    conn.close()
    return jsonify({'received': data, 'status': 'success'})


if __name__ == "__main__":
    app.run(port=5000)
