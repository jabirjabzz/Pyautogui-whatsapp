import os
import pyautogui as pg
import time
import sys
import cv2
import numpy as np
from pywinauto import Application, keyboard
import pywinauto
import time

# Path to VS Code executable
vscode_path = r"C:\Users\<YourUsername>\AppData\Local\Programs\Microsoft VS Code\Code.exe"
user = 'jabzz'
def automate_vscode_commands():
    # Step 1: Launch Visual Studio Code
    app = Application(backend="uia").start(vscode_path)
    
    # Wait for VS Code to load
    time.sleep(5)  # Adjust based on loading time

    # Step 2: Set focus to the VS Code window
    vscode_window = app.window(title_re=".*Visual Studio Code.*")
    vscode_window.set_focus()
    
    # Step 3: Open a new terminal using Ctrl+` shortcut
    keyboard.send_keys("^`")  # Ctrl + ` to open terminal
    time.sleep(2)  # Allow terminal to open

    # Step 4: Type and execute the commands in the terminal
    commands = [
        "git add .",
        "git add -u",
        'git commit -m "save and continue"',
        "git checkout main",
        "git push origin main",
        "scrapy crawl malayalam_spider"
    ]
    
    for cmd in commands:
        keyboard.send_keys(cmd)
        keyboard.send_keys("{ENTER}")  # Press Enter
        time.sleep(2)  # Adjust delay if needed

if __name__ == "__main__":
    
    
def open_whatsapp():
    try:
        pg.hotkey('win', 's')  
        time.sleep(1)
        pg.typewrite('WhatsApp')  
        time.sleep(1)
        pg.press('enter')  
        time.sleep(5)  
    except Exception as e:
        print(f"Error opening WhatsApp: {e}")
        sys.exit(1)

def perform_main_steps():
    try:
        pg.hotkey('ctrl', 'f')  
        time.sleep(1)
        pg.hotkey('ctrl', 'a')  
        time.sleep(1)
        pg.press('backspace')  
        pg.typewrite(user)  
        time.sleep(1)
        pg.press('down')  
        time.sleep(1)
        pg.press('enter')  
        time.sleep(1)
        for _ in range(11):  
            pg.press('tab')
            time.sleep(0.2)
        pg.press('enter')  
        time.sleep(5)  
    except Exception as e:
        print(f"Error in main steps: {e}")
        sys.exit(1)

def find_image(image_path, confidence_threshold=0.75):
    time.sleep(10)
    try:
        # Read the image
        template = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if template is None:
            print(f"Failed to read image: {image_path}")
            return False

        # Take a screenshot
        screenshot = pg.screenshot()
        screenshot_gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

        # Perform template matching
        result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
        
        # Find the maximum correlation
        _, max_val, _, _ = cv2.minMaxLoc(result)
        
        print(f"Image match confidence: {max_val}")
        
        # Check if confidence is within the specified range
        return max_val >= confidence_threshold
    
    except Exception as e:
        print(f"Error finding image: {e}")
        return False
def type_character_by_character(text, delay=0.1):
    """
    Types a given text character by character with a delay.

    Args:
        text (str): The text to be typed.
        delay (float): Delay between typing each character (in seconds).
    """
    for char in text:
        pg.typewrite(char)
        time.sleep(delay)  # Add a delay between typing each character
    print("Finished typing!")

def handle_response(timeout=300):
    # def click_image(location):
    #     # Get the center of the image
    #     x, y = pg.center(location)
    #     # Click the center
    #     pg.click(x, y)
    #     print(f"Clicked on image at {x}, {y}")
    
        
    shut_down_image = os.path.join(
        "C:", os.sep, "Users", "Administrator", "Documents", "GitHub", "Pyautogui", "images", "Screenshot 2024-11-28 110644.png"
    )
    save_image = os.path.join(
        "C:", os.sep, "Users", "Administrator", "Documents", "GitHub", "Pyautogui", "images", "Screenshot 2024-11-28 110415.png"
    )

    if not all(os.path.exists(img) for img in [shut_down_image, save_image]):
        print("Error: One or more image files not found.")
        sys.exit(1)

    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            if find_image(shut_down_image):
                print("Detected 'Shut down' response.")
                open_whatsapp()
                time.sleep(2)
                type_character_by_character("shutting down..", delay=0.2)
                time.sleep(2)
                pg.press('enter')
                time.sleep(1)
                pg.hotkey('win', 'r')
            #   pg.press('enter')
                return

            if find_image(save_image):
                print("Detected 'Save' response.")
                open_whatsapp()
                time.sleep(2)
                type_character_by_character("Saving..", delay=0.2)
                time.sleep(2)
                pg.press('enter')
                automate_vscode_commands()
                return

            time.sleep(1)
        except Exception as e:
            print(f"Error during image detection: {e}")
            break

    print("Timeout reached or unexpected error.")
    sys.exit(1)
# location = pg.locateOnScreen(image_path, confidence=confidence_level)
# image_location = find_image(image_path, confidence)
def main():
    open_whatsapp()
    perform_main_steps()
    handle_response()

if __name__ == "__main__":
    main()
