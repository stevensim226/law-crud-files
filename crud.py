from database import select_all, create_note, delete_note, update_note, save_pict
from flask import Flask, jsonify, request

app = Flask(__name__)

"""
CRUD for Notes
"""

@app.route("/get-notes", methods=["GET"])
def get_note_view():
    return jsonify({
        "data": select_all()
    })

@app.route("/create-note", methods=["POST"])
def create_note_view():
    new_note = create_note(
        title=request.json["title"],
        note=request.json["note"]
    )
    return jsonify({
        "data": new_note
    })

@app.route("/delete-note", methods=["DELETE"])
def delete_note_view():
    deleted_note = delete_note(request.json["title"])
    return jsonify({
        "data": deleted_note
    })

@app.route("/update-note", methods=["PUT"])
def update_note_view():
    updated_note = update_note(
        title=request.json["title"],
        note=request.json["note"]
    )
    return jsonify({
        "data": updated_note
    })

"""
C for Pictures
"""
@app.route("/create-picture", methods=["POST"])
def create_picture_view():
    return jsonify(save_pict(request.files["attachment"]))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
