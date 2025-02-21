#!/usr/bin/env python3
import wx
from api import send_request
from controller import delete_selection, get_clipboard, handle_selection, paste_clipboard, send_to_clipboard
from gui import show_selection_dialog, show_refine_dialog

def main():
    # Read data from the clipboard using pyperclip
    app = wx.App(False)
    handle_selection()

    clipboard = get_clipboard()
    original_sentence = clipboard  # Store the original sentence
    delete_selection()

    # Call the API
    improved_sentences = send_request(original_sentence)

    while True:
        # Show selection dialog
        if improved_sentences:
            print(improved_sentences)
            selected_sentence, action = show_selection_dialog(improved_sentences)
        else:
            selected_sentence, action = None, 'cancel'

        if action == 'ok':
            print("ok")
            improved_sentence = selected_sentence if selected_sentence else clipboard
            send_to_clipboard(improved_sentence)
            break
        elif action == 'refine':
            instructions = show_refine_dialog()
            if instructions:
                #

                improved_sentences = send_request(
                    original_sentence,
                    previous_outputs=improved_sentences,
                    extra_instructions=instructions
                )
            else:
                # If user cancels, return to selection dialog
                continue
        else:  # 'cancel'
            send_to_clipboard(selected_sentence)
            break
    paste_clipboard()

if __name__ == "__main__":
    main()
