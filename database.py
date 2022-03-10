from datetime import datetime

DATABASE = []

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
    return [note.serialize() for note in DATABASE]

def create_note(title, note):
    new_note = Note(title, note)
    DATABASE.append(new_note)
    return new_note.serialize()

def delete_note(title):
    for note in DATABASE:
        if note.title == title:
            DATABASE.remove(note)
            return note.serialize()
    else:
        return None

def update_note(title, note):
    for notecls in DATABASE:
        if notecls.title == title:
            notecls.note = note
            return notecls.serialize()
    else:
        return None

def save_pict(file):
    time_str = datetime.now().strftime("%Y%m%d-%H%M%S")
    filepath = f"./pictures/{time_str}-{file.filename}"
    file.save(filepath)
    return {
        "status": "saved",
        "path": filepath
    }