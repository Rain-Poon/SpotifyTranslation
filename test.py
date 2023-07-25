import pyautogui
import time


def capture_screen_with_box(x1, y1, x2, y2):
    """Captures a screenshot of the screen and draws a box around the specified area.

    Args:
      x1: The x-coordinate of the top-left corner of the box.
      y1: The y-coordinate of the top-left corner of the box.
      x2: The x-coordinate of the bottom-right corner of the box.
      y2: The y-coordinate of the bottom-right corner of the box.

    Returns:
      A screenshot of the specified area.
    """

    screenshot = pyautogui.screenshot()
    return screenshot


if __name__ == "__main__":
    x1, y1, x2, y2 = 100, 100, 200, 200
    screenshot = capture_screen_with_box(x1, y1, x2, y2)
    screenshot.show()