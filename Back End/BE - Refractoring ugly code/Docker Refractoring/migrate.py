import app

with open('schema.sql') as s:
    app.db.cursor.executescript(s.read())

print("SQLite database (re)created")
