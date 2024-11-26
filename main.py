#!/usr/bin/env python3
import sys
import pyperclip
from loguru import logger
import wx
from api import send_request
from gui import show_selection_dialog

def main():
    app = wx.App(False)  # Initialize the wx App

    # Read data from the clipboard using pyperclip
    clipboard = pyperclip.paste().strip()
    if not clipboard:
        logger.error("Clipboard is empty.")
        sys.exit(1)

    # Call the API
    improved_sentences = send_request(clipboard)

    # Show selection dialog
    if improved_sentences:
        selected_sentence = show_selection_dialog(improved_sentences)
        improved_sentence = selected_sentence if selected_sentence else clipboard
    else:
        improved_sentence = clipboard

    # Set data to the clipboard using pyperclip
    pyperclip.copy(improved_sentence)
    logger.info(f"Clipboard text '{improved_sentence}' set successfully.")

if __name__ == "__main__":
    main()
