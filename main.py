import pyautogui as pg
import time

def open_whatsapp():
    # Step 1: Open WhatsApp from the taskbar search
    pg.hotkey('win', 's')  # Open search in the taskbar
    time.sleep(1)
    pg.typewrite('WhatsApp')  # Type WhatsApp
    time.sleep(1)
    pg.press('enter')  # Press Enter to open WhatsApp
    time.sleep(5)  # Wait for WhatsApp to open

def perform_main_steps():
    # Steps 3-6
    pg.hotkey('ctrl', 'f')  # 'Ctrl + F'
    time.sleep(1)
    pg.hotkey('ctrl', 'a')  # 'Ctrl + A'
    time.sleep(1)
    pg.press('backspace')  # Clear the search
    pg.typewrite('aamzz')  # Type 'aamzz'
    time.sleep(1)
    pg.press('down')  # Arrow down
    time.sleep(1)
    pg.press('enter')  # Press Enter
    time.sleep(1)
    for _ in range(11):  # Press Tab 11 times
        pg.press('tab')
        time.sleep(0.2)
    pg.press('enter')  # Press Enter
    time.sleep(5)  # Wait for a response

def wait_for_image(image_path, timeout=300):
    """Wait until the image appears on the screen or the timeout is reached."""
    start_time = time.time()
    while True:
        location = pg.locateOnScreen(image_path, confidence=0.8)  # Match with 80% confidence
        if location:
            return location
        if time.time() - start_time > timeout:
            print(f"Timeout reached while waiting for {image_path}.")
            return None
        time.sleep(1)  # Check every second

def handle_response():
    # Wait for either "Shut down" or "Save" image
    print("Waiting for response...")
    shut_down_image = 'shut_down_image.png'  # Replace with the actual image path for "Shut down"
    save_image = 'save_image.png'  # Replace with the actual image path for "Save"

    while True:
        if pg.locateOnScreen(shut_down_image, confidence=0.8):
            print("Detected 'Shut down' response.")
            # Sub-steps for "Shut down"
            perform_main_steps()
            pg.typewrite('shutting down')  # Type 'shutting down'
            pg.press('enter')  # Press Enter
            time.sleep(1)
            pg.hotkey('win', 'r')  # Open Run dialog
            break
        elif pg.locateOnScreen(save_image, confidence=0.8):
            print("Detected 'Save' response.")
            # Sub-steps for "Save"
            perform_main_steps()
            pg.typewrite('Saving')  # Type 'Saving'
            pg.press('enter')  # Press Enter
            break
        time.sleep(1)  # Check every second

# Main program
open_whatsapp()
perform_main_steps()
handle_response()