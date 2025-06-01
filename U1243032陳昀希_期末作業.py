from inputimeout import inputimeout, TimeoutOccurred
import time
import sys

def timed_input(prompt, timeout):
    try:
        sys.stdout.write(f"⏳ 你有 {timeout} 秒可以作答...\n")
        sys.stdout.flush()
        return inputimeout(prompt=prompt, timeout=timeout)
    except TimeoutOccurred:
        print("⌛ 時間到！")
        return None

def is_valid_number(text):
    return text.isdigit() and 1 <= int(text) <= 100
