import platform
import time
from loguru import logger
import pyperclip
import pyautogui

def send_to_clipboard(content):
    pyperclip.copy(content)
    logger.info(f"Clipboard text '{content}' set successfully.")

def paste_clipboard():
    time.sleep(0.1)
    pyautogui.hotkey("ctrl", "v")

def handle_selection():
    logger.debug("Copying to clipboard...")
    pyautogui.hotkey("ctrl", "c")
    logger.debug("Copied to clipboard.")

def get_clipboard():
    logger.debug("Reading clipboard...")
    clipboard = pyperclip.paste()
    if not clipboard:
        raise Exception("No text selected or clipboard is empty.")
    logger.debug("Read clipboard.")
    return clipboard

def delete_selection():
    pyautogui.hotkey("backspace")
