import os
import pyautogui
import time
import json

chrome_path = r'"C:/Program Files/Google/Chrome/Application/chrome.exe"' # Change this to your Chrome path
url = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'

os.system(f'{chrome_path} --incognito {url}')

time.sleep(10)  

with open('login\Co-Ordinates\coordinates_and_values.json', 'r') as file:
    actions = json.load(file)

for action in actions:
    pyautogui.moveTo(action['x'], action['y'], duration=1)
    
    pyautogui.click(clicks=action['clicks'], interval=action['interval'])

    if action['typingValue']:
        pyautogui.typewrite(action['typingValue'], interval=0.25)

    time.sleep(1)

print("Action sequence completed.")
