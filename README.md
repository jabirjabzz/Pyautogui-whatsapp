# WhatsApp Automation with VS Code Integration

This Python script automates tasks within WhatsApp and interacts with Visual Studio Code (VS Code) using `pyautogui` for UI automation and `pywinauto` for VS Code control. It's designed to streamline specific workflows, such as triggering Git actions and receiving notifications in WhatsApp based on on-screen events.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Features

*   **WhatsApp Launch:** Automatically opens the WhatsApp desktop application.
*   **Customizable WhatsApp Actions:** Provides a framework (`perform_main_steps`) for defining custom actions within WhatsApp (e.g., sending messages, navigating menus). *This requires further implementation based on your specific needs.*
*   **VS Code Integration:** Automates common Git commands (add, commit, push) within a VS Code terminal, along with running a Scrapy spider.
*   **Image Recognition:** Uses OpenCV (`cv2`) to detect on-screen images ("Shut down" and "Save") and trigger corresponding actions.
*   **WhatsApp Notifications:** Sends WhatsApp messages based on detected events (e.g., "shutting down," "saving").

## Important Considerations

*   **WhatsApp Automation Customization:** The `perform_main_steps` function is a placeholder. You *must* implement the actual WhatsApp actions you want to automate using `pyautogui`.
*   **Image Paths:** The script relies on image recognition. Ensure the paths to the "Shut down" and "Save" images (`shut_down_image`, `save_image` in `handle_response()`) are correct. These are currently hardcoded and *need to be changed*.
*   **VS Code Path:** Verify the `vscode_path` variable points to your VS Code executable.
*   **Timing:** The script uses `time.sleep()` for delays. Adjust these values as needed based on your system's performance.
*   **Error Handling:** Basic error handling is included, but more robust error management may be needed for production use.
*   **Security:** Be mindful of the security implications of UI automation. Avoid automating sensitive actions or storing credentials in the script.
*   **Cross-Platform Compatibility:** This script is primarily designed for Windows due to its use of `pywinauto`. Adapting it to other operating systems would require significant modifications.

## Getting Started

1.  **Clone the Repository:**

    ```bash
    git clone [invalid URL removed] # Replace with your repo URL
    cd YOUR_REPO_NAME
    ```

2.  **Install Dependencies:**

    ```bash
    pip install pyautogui opencv-python pywinauto
    ```

3.  **Configure Image Paths:**

    *   **Capture Images:** Take screenshots of the "Shut down" and "Save" buttons/areas you want to detect.
    *   **Update Paths:** Modify the `shut_down_image` and `save_image` variables in the `handle_response` function to point to the correct locations of your image files. Example:

        ```python
        shut_down_image = r"C:\path\to\your\shutdown_image.png"
        save_image = r"C:\path\to\your\save_image.png"
        ```

4.  **Configure VS Code Path:**

    *   Set the `vscode_path` variable to the correct path of your VS Code executable. Example:

        ```python
        vscode_path = r"C:\Users\YourUsername\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        ```

5.  **Implement WhatsApp Actions:**

    *   Edit the `perform_main_steps` function to add the `pyautogui` commands that simulate the desired actions within WhatsApp.

6.  **Run the Script:**

    ```bash
    python main.py
    ```

## Code Structure

*   `main.py`: The main script containing the automation logic.
*   `images/`: (Create this directory) This is where you should store the "Shut down" and "Save" images.

## Example Usage (Conceptual)

The script is designed to be triggered by an external event (e.g., a process completing). When run, it will:

1.  Open WhatsApp.
2.  Perform the actions defined in `perform_main_steps`.
3.  Continuously check for the "Shut down" or "Save" images.
4.  If "Shut down" is detected, send a WhatsApp message and potentially perform a system shutdown (not implemented by default).
5.  If "Save" is detected, send a WhatsApp message and execute the VS Code Git commands.


## Contributing
## we can customize as your wish and contribute it what you explored!!
Contributions are welcome! Please open an issue or submit a pull request.
