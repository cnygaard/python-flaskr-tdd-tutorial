import sqlite3
from flask import Flask, g # Import Flask web framework

# database 
DATABASE = "flaskr.db"

# init flask application
app = Flask(__name__)

# Load config
app.config.from_object(__name__)

# connect to database
def connect_db():
    # Connects to database
    rv = sqlite3.connect(app.config["DATABASE"])
    rv.row_factory = sqlite3.Row
    return rv

# init database
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource("schema.sql", mode="r") as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    if not hasattr(g, "sqlite_db"):
        g.sqlite_db = connect_db()
    return g.sqlite_db

# clode database connection
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "sqlite_db"):
        g.sqlite_db.close()

# Add root url route
@app.route("/")
def hello():
    return "Hello, World!" # Return hello world from root URL

# Run the Flask application
if __name__ == "__main__":
    app.run()
