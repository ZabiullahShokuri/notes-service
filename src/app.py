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
print("Before removing:")
manager.display_notes()

removed = manager.remove_note("First Note")

print("After removing:")
manager.display_notes()

print("Removed:", removed)
