class Editor:
    def view_document(self):
        print("Viewing document")

    def edit_document(self):
        print("Editing documents is not available in the free version")


class ProEditor(Editor):
    def edit_document(self):
        print("Editing document")


license_key = input("Enter license key: ")

if license_key == "12345":  # Assuming "12345" is the correct license key
    editor = ProEditor()
else:
    editor = Editor()

editor.view_document()
editor.edit_document()