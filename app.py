# to run this website and watch for changes:
# $ export FLASK_ENV=development; flask run


from flask import Flask, g, render_template, request

import sqlite3

import io
import base64


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main_better.html')


@app.route('/view/')
def view():
    return render_template('view.html')


def get_message_db():
    if 'message_db' not in g:
        g.message_db = sqlite3.connect("messages_db.sqlite")
        cursor = g.message_db.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages(
            id int,
            handle varchar(255),
            message varchar(255)
        )""")
    return g.message_db


def insert_message(request):
    msg = request.form['message']
    hnd = request.form['handle']
    db = get_message_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(id) FROM messages")
    # set id as number of rows of messages
    id = cursor.fetchone()[0]
    cmd = """
    INSERT INTO messages (id, handle, message)
    VALUES (""" + str(id) + """,' """ + hnd + """','""" + msg + """')
    """
    cursor.execute(cmd)
    db.commit()
    db.close()
    return msg, hnd


@app.route('/submit/', methods=['POST', 'GET'])
def submit():
    if request.method == 'GET':
        return render_template('submit.html')
    else:
        insert_message(request=request)
        return render_template('submit.html', thanks=True)
