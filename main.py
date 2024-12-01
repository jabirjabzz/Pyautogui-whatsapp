import os
import pyautogui as pg
import time
import sys
import cv2
import numpy as np

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
        pg.typewrite('aamzz')  
        time.sleep(1)
        pg.press('down')  
        time.sleep(1)
        pg.press('enter')  
        time.sleep(1)
        for _ in range(11):  
            pg.press('tab')
            time.sleep(0.2)
        pg.press('enter')  
        time.sleep(30)  
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
                pg.typewrite('shutting down')
                time.sleep(2)
                pg.press('enter')
                time.sleep(1)
                pg.hotkey('win', 'r')
                return

            if find_image(save_image):
                print("Detected 'Save' response.")
                open_whatsapp()
                time.sleep(2)
                pg.typewrite('Saving')
                time.sleep(2)
                pg.press('enter')
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