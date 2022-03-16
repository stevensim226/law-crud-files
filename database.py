import psycopg2
import os
from datetime import datetime

DB_CONN = conn = psycopg2.connect(
    dbname=os.environ.get("DB_NAME"),
    user=os.environ.get("DB_USER"),
    host=os.environ.get("DB_HOST"),
    password=os.environ.get("DB_PASSWORD")
)
DB_CURR = DB_CONN.cursor()
DB_CURR.execute("CREATE TABLE IF NOT EXISTS notes (title VARCHAR(50), note VARCHAR(1000));")
DB_CONN.commit()

class Note:
    def __init__(self, title, note):
        self.title = title # "Primary Key"
        self.note = note

    def serialize(self):
        return {
            "title": self.title,
            "note": self.note
        }

def select_all():
    DB_CURR.execute("SELECT title, note FROM notes;")
    return [Note(title, note).serialize() for title, note in DB_CURR.fetchall()]

def create_note(title, note):
    DB_CURR.execute(f"INSERT INTO notes (title, note) VALUES ('{title}', '{note}')")
    DB_CONN.commit()
    new_note = Note(title, note)
    return new_note.serialize()

def delete_note(title):
    DB_CURR.execute(f"DELETE FROM notes WHERE title = '{title}'")
    DB_CONN.commit()
    return None

def update_note(title, note):
    DB_CURR.execute(f"UPDATE notes SET note = '{note}' WHERE title = '{title}'")
    DB_CONN.commit()
    return None

def save_pict(file):
    time_str = datetime.now().strftime("%Y%m%d-%H%M%S")
    filepath = f"./pictures/{time_str}-{file.filename}"
    file.save(filepath)
    return {
        "status": "saved",
        "path": filepath
    }