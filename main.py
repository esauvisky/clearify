#!/usr/bin/env python3
import wx
from gui import show_selection_dialog
from api import send_request_with_gemini
from controller import delete_selection, get_clipboard, handle_selection, paste_clipboard, send_to_clipboard

def main():
    handle_selection()
    clipboard = get_clipboard()
    delete_selection()
    original_sentence = clipboard
    try:
        # Call the API
        improved_sentences = send_request_with_gemini(original_sentence)

        app = wx.App(False)

        # Show selection dialog
        if improved_sentences:
            selected_sentence, action = show_selection_dialog(improved_sentences)
        else:
            selected_sentence, action = original_sentence, 'cancel'

        if action == 'ok':
            improved_sentence = selected_sentence if selected_sentence else original_sentence
            send_to_clipboard(improved_sentence)
        else:
            raise Exception("No selection made.")
    except Exception as e:
        send_to_clipboard(original_sentence)
    finally:
        paste_clipboard()

if __name__ == "__main__":
    main()
