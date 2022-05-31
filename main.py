from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import pyautogui
import numpy as np
import cv2
import matplotlib.pyplot as plt
import time
import pytesseract


opts = Options()
opts.headless = False
# assert opts.headless  # Operating in headless mode
opts.add_argument('--no-sandbox')
opts.add_argument('--disable-dev-shm-usage')


# browser = Firefox(options=opts)


# URL = 'https://www.zillow.com/'
# browser.get(URL)
# search_form = browser.find_element(By.XPATH,
#                                    '/html/body/main/div[1]/div[2]/div[2]/div/div[2]/div/div/form/div/div[1]/input')
# search_form.send_keys('pacific coast, CA')
# search_form.submit()


def get_position():
    """
    Gets the mouse coordinates
    return: the coordinates
    """
    return pyautogui.position()


# def get_screenshot(x_lcorner,y_lcorner, width, height ) :
def get_screenshot():
    """
    Gets coordinnates and "screenshot" accordingly
    return: the crop image
    """

    # Get the starting point from the mouse position
    # x_y = pyautogui.position()

    res = input('Are you ready with the mouse position for the top-left corner? Y/N')

    tlx = 0
    tly = 0
    rbx = 0
    rby = 0

    if res.upper() == 'Y':
        # Get the starting point from the mouse position
        tlx, tly = pyautogui.position()
        print(tlx)
        print(tly)

    res = input('Are you ready with the mouse position for the bottom-right corner? Y/N')

    if res.upper() == 'Y':
        # Get the starting point from the mouse position
        rbx, rby = pyautogui.position()
        print(rbx)
        print(rby)

    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    return image[tly:rby, tlx:rbx, :3]  # image[ymin:ymax,xmin:xmax]


def extract_address(tlx=1133, tly=297, rbx=1627, rby=340):
    """Extract the address from the Zillow website based on the user screen size

    :return:
    """
    assert pyautogui.size() == (1920, 1080)
    return extract_crop(tlx=1133
                        , tly=297
                        , rbx=1627
                        , rby=340)


def extract_crop(tlx, tly, rbx, rby):
    """Extract a crop

    :param tlx:int x top left position
    :param tly:int y top left position
    :param rbx:int x top right position
    :param rby:int y top right position
    :return:
    """
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    return image[tly:rby, tlx:rbx, :3]  # image[ymin:ymax,xmin:xmax]

time.sleep(3)
if __name__ == '__main__':
    crop_address = extract_address()

    get_screenshot()
    plt.imshow(crop_address)
    # plt.imshow(image)
    plt.show()
