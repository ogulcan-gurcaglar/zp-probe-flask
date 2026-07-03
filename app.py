import sqlite3
from flask import Flask, request

app = Flask(__name__)


@app.route("/user")
def user():
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    uid = request.args.get("id", "")
    # SQL injection: unsanitized request param concatenated into the query.
    cur.execute("SELECT * FROM users WHERE id = '" + uid + "'")
    return {"rows": [list(r) for r in cur.fetchall()]}


if __name__ == "__main__":
    app.run()
