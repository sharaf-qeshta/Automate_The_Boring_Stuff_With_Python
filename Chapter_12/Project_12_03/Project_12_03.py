"""
2048
2048 is a simple game where you combine tiles by sliding them up, down,
left, or right with the arrow keys. You can actually get a fairly high score
by repeatedly sliding in an up, right, down, and left pattern over and over
again. Write a program that will open the game at https://gabrielecirulli
.github.io/2048/ and keep sending up, right, down, and left keystrokes to
automatically play the game.


@author Sharaf Qeshta
"""

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import random

browser = webdriver.Chrome()
browser.get("https://gabrielecirulli.github.io/2048/")
browser.fullscreen_window()
root_element = browser.find_element(By.TAG_NAME, "html")

arrows = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]
while True:
    root_element.send_keys(random.randint(0, 3))
