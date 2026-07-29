class NotesManager:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def display_notes(self):
        for note in self.notes:
            note.display()
            print("-" * 30)

    def remove_note(self, title):
        for note in self.notes:
            if note.title == title:
                self.notes.remove(note)
                return True

        return False

    def find_note(self, title):
        for note in self.notes:
            if note.title == title:
                return note

        return None

    def update_note(self, title, new_content):
        note = self.find_note(title)

        if note:
            note.content = new_content
            return True

        return False
