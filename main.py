#!/usr/bin/env python3
import wx
from api import send_request
from controller import delete_selection, get_clipboard, handle_selection, paste_clipboard, send_to_clipboard
from gui import show_selection_dialog

def main():
    # Read data from the clipboard using pyperclip
    handle_selection()
    clipboard = get_clipboard()
    try:
        delete_selection()

        # Call the API
        improved_sentences = send_request(clipboard)

        # Show selection dialog
        if improved_sentences:
            selected_sentence = show_selection_dialog(improved_sentences)
            improved_sentence = selected_sentence if selected_sentence else clipboard
        else:
            improved_sentence = clipboard

        send_to_clipboard(improved_sentence)
    finally:
        paste_clipboard()



if __name__ == "__main__":
    main()
