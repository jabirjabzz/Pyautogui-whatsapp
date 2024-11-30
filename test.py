import os
import pyautogui as pg
import time
import cv2

# Define image paths at the top of the script
SHUT_DOWN_IMAGE = os.path.join(
    "C:", os.sep, "Users", "Administrator", "Documents", "GitHub", "Pyautogui", "images", "Screenshot 2024-11-28 110644.png"
)
SAVE_IMAGE = os.path.join(
    "C:", os.sep, "Users", "Administrator", "Documents", "GitHub", "Pyautogui", "images", "Screenshot 2024-11-28 110415.png"
)

def handle_response():
    print("Waiting for response...")
    
    # Verify file exists before attempting to use it
    if not os.path.exists(SHUT_DOWN_IMAGE):
        print(f"Error: Shut down image file not found at {SHUT_DOWN_IMAGE}")
        return
    
    if not os.path.exists(SAVE_IMAGE):
        print(f"Error: Save image file not found at {SAVE_IMAGE}")
        return
    
    # Rest of the existing code...
    while True:
        if pg.locateOnScreen(SHUT_DOWN_IMAGE, confidence=0.8):
            # Your existing "Shut down" handling code
            pass
        
        if pg.locateOnScreen(SAVE_IMAGE, confidence=0.8):
            # Your existing "Save" handling code
            pass
        
        time.sleep(1)
