# Auto Cursor Movement on File Script

This Python script automates keyboard right arrow key and pressing right arrow key to move through a document or file using the `pyautogui` library. It provides functionality to pause and resume moving based on user input, specifically using the `Esc` key.

## Features

- **Movement Automation**: Moves the cursor to the start of the file and move to the end by simulating right arrow key presses.
- **Pause Functionality**:
  - Press `Esc` once to pause the script for 10 seconds.
  - Press `Esc` and hold it for more than 0.5 seconds, then press `Esc` twice to pause the script.
  - Press `Esc` twice to resume scrolling when the script is paused.

## Prerequisites

- **Python**: Ensure Python 3.x is installed on your system.
- **Required Libraries**: Install the required Python libraries using `pip`.

## Installation

1. **Clone the Repository** (if applicable):
   ```sh
   git clone https://github.com/imparth7/keyboard-automation.git
   cd keyboard-automation
   ```

2. **Install Required Libraries**:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. **Prepare Your Document**:
   - Make sure the document or file you want to move through is in focus.

2. **Run the Script**:
   ```sh
   python main.py
   ```

3. **Controlling the Script**:
   - **Press `Esc` once**: Pauses the script for 10 seconds.
   - **Hold `Esc` for more than 0.5 seconds**: Switches to waiting for a double `Esc` press.
   - **Press `Esc` twice**: Toggles the pause state. The script will resume if it was paused.

## Notes

- Ensure that the document or window you want to move through is active and focused when running the script.
- Adjust the sleep durations in the script if necessary to match your system’s performance and responsiveness.

## Troubleshooting

- **Script Not Scrolling**: Verify that the document is focused and the right arrow key moves the cursor as expected. Adjust the sleep times if needed.
- **Key Presses Not Detected**: Ensure the `keyboard` library has the necessary permissions and that no other program is intercepting key presses.

## License

This project is licensed under the MIT License.

## Contact

For any questions or issues, please contact me [imparth](https://github.com/imparth7) or open an issue on the [GitHub repository](https://github.com/imparth7/keyboard-automation/issues).