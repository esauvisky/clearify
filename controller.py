import platform
import time
from loguru import logger
from pynput.keyboard import Key, Listener, Controller
import pyperclip

# Keyboard controller to simulate typing
keyboard = Controller()

def send_to_clipboard(content):
    pyperclip.copy(content)
    logger.info(f"Clipboard text '{content}' set successfully.")

def paste_clipboard():
    time.sleep(0.1)
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl)

def handle_selection():
    # Simulate copying the selection to clipboard
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release('c')
    keyboard.release(Key.ctrl)

def get_clipboard():
    # Read data from the clipboard using pyperclip
    clipboard = pyperclip.paste().strip()
    if not clipboard:
        raise Exception("No text selected or clipboard is empty.")
    return clipboard

def delete_selection():
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)
