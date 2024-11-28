import cv2

file_path = r"C:\Users\Administrator\Documents\GitHub\Pyautogui\images\Screenshot 2024-11-28 110644.png"
image = cv2.imread(file_path)
if image is None:
    print("Failed to load the image. Check the file path or format.")
else:
    print("Image loaded successfully!")

