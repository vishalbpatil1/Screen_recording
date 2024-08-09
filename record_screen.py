import cv2
import numpy as np
import pyautogui
import time

class ScreenRecorder:
    def __init__(self, filename="output.avi", fps=60.0):
        # Define screen size (you can change this if needed)
        self.screen_size = pyautogui.size()
        self.fps = fps
        self.filename = filename
        self.is_recording = False
        self.out = None
        self.start_time = None

    def start_recording(self):
        if self.is_recording:
            print("Recording is already in progress.")
            return
        
        self.is_recording = True
        self.start_time = time.time()
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        self.out = cv2.VideoWriter(self.filename, fourcc, self.fps, self.screen_size)
        print(f"Started recording to {self.filename}")

        # Start the recording loop
        while self.is_recording:
            # Capture the screen
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            self.out.write(frame)

            # Break out of loop if the recording time exceeds a specified limit
            if time.time() - self.start_time > 10:  # Stop recording after 10 seconds for demonstration
                self.stop_recording()

    def stop_recording(self):
        if not self.is_recording:
            print("No recording in progress.")
            return
        
        self.is_recording = False
        self.out.release()
        print(f"Stopped recording and saved to {self.filename}")

    def capture_screenshot(self, filename="screenshot.png"):
        img = pyautogui.screenshot()
        img.save(filename)
        print(f"Screenshot saved to {filename}")

if __name__ == "__main__":
    recorder = ScreenRecorder(filename="recording.avi")

    # Example usage
    recorder.start_recording()
    time.sleep(30)  # Record for 5 seconds
    recorder.stop_recording()
    
    # Take a screenshot
    recorder.capture_screenshot("screenshot.png")
