import pyautogui as pg

shut_down_image = r"C:\Users\Administrator\Documents\GitHub\Pyautogui\images\Screenshot 2024-11-28 110644.png"

try:
    result = pg.locateOnScreen(shut_down_image, confidence=0.8)
    if result:
        print("Image found:", result)
    else:
        print("Image not found.")
except Exception as e:
    print("Error:", e)
