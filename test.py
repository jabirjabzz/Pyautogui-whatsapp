import cv2
import pyautogui as pg
import numpy as np

def locate_image(image_path, confidence=0.8):
    screenshot = pg.screenshot()
    screen_array = np.array(screenshot)
    screen_gray = cv2.cvtColor(screen_array, cv2.COLOR_BGR2GRAY)

    needle = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if needle is None:
        print("Error: Could not read the image file.")
        return None

    result = cv2.matchTemplate(screen_gray, needle, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= confidence)

    points = list(zip(*loc[::-1]))
    return points

image_path = r"C:\Users\Administrator\Documents\GitHub\Pyautogui\images\Screenshot 2024-11-28 110644.png"
matches = locate_image(image_path, confidence=0.7)

if matches:
    print("Image found at:", matches)
else:
    print("Image not found.")
