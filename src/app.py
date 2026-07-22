from note import Note
from manager import NotesManager

print("Notes Manager Started")

manager = NotesManager()

manager.add_note(
    Note(
        "First Note",
        "Learning Git and Python step by step."
    )
)

manager.add_note(
    Note(
        "Second Note",
        "Practicing Git workflow."
    )
)

manager.display_notes()
