import pyautogui
import keyboard
import time

def process_file():
    global paused, waiting_for_double_press, esc_press_start_time

    # Simulate Ctrl+Home to move the pointer to the start of the file
    pyautogui.hotkey("ctrl", "home")
    time.sleep(1)  # Wait for 1 second to make sure the pointer is at the start

    while True:
        current_time = time.time()

        # Check if `Esc` is pressed and held
        if keyboard.is_pressed("esc"):
            if esc_press_start_time is None:
                esc_press_start_time = current_time
            elif current_time - esc_press_start_time > 0.5:
                # If `Esc` is held for more than 0.5 seconds, wait for double press
                waiting_for_double_press = True
                esc_press_start_time = None
                print("Press Esc twice to pause.")
        else:
            if esc_press_start_time is not None and (current_time - esc_press_start_time <= 0.5):
                # If `Esc` was pressed briefly, pause for 10 seconds
                print("Esc pressed once. Pausing for 10 seconds...")
                time.sleep(10)
                esc_press_start_time = None
                print("10 seconds completed. Resume ...")
            
            # Reset the start time if the key was not pressed
            esc_press_start_time = None

        if paused:
            while paused:
                if keyboard.is_pressed("esc"):
                    time.sleep(0.15)  # Short delay to ensure the key press is registered
                    if keyboard.is_pressed("esc"):
                        print("Esc pressed twice. Resuming...")
                        paused = False
                        waiting_for_double_press = False
                time.sleep(0.1)  # Short delay to prevent high CPU usage
            continue  # Resume the outer loop once unpaused

        if waiting_for_double_press and keyboard.is_pressed("esc"):
            time.sleep(0.15)  # Short delay to ensure the key press is registered
            if keyboard.is_pressed("esc"):
                print("Esc pressed twice. Pausing...")
                paused = True
                waiting_for_double_press = False
                print("Paused.\nPress Esc twice to resume.")
        
        pyautogui.press("right")
        time.sleep(0.2)  # Add a small delay to avoid overwhelming the system

# Initialize the paused state and other variables
paused = False
waiting_for_double_press = False
esc_press_start_time = None

# Main function to start the processing
if __name__ == "__main__":
    time.sleep(1)  # Initial delay to ensure focus
    process_file()
