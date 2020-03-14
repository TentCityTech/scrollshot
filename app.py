# import modules
import pyautogui
import time


x = 1
# insert how many screenshots you want to take example '10' screenshots.
while x < 10:
    pyautogui.screenshot(
        (
            "/Users/User/Desktop/filename"
            + str(x)
            + ".png"
        ),
        # Crop the screenshot. (left, top, width, height)
        region=(500, 100, 600, 800),
    )
    # Scroll the window and prep for new screenshot.
    pyautogui.scroll(-30, x=2118, y=495)
    x += 1
    # Wait 2 seconds before taking the next screenshot.
    time.sleep(2)
