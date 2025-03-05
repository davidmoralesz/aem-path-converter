import logging
from pynput import keyboard
from .converter import format_clipboard
from .config import HOTKEY

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def on_activate():
    """
    Callback function triggered when the hotkey is pressed.
    """
    format_clipboard()


def start_hotkey_listener():
    """
    Starts listening for the global hotkey.
    """
    logging.info(
        "Starting hotkey listener. Press Cmd + Shift + . to format clipboard content."
    )
    with keyboard.GlobalHotKeys({HOTKEY: on_activate}) as h:
        h.join()
