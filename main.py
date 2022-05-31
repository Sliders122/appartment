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

pytesseract.pytesseract.tesseract_cmd = "C:\\Users\Quentin\AppData\Local\Programs\Tesseract-OCR\\tesseract.exe"
#C:\Users\Quentin\AppData\Local\Programs\Tesseract-OCR
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
    tlx = 0
    tly = 0
    rbx = 0
    rby = 0

    # We wait for any the user input to put his mouse on the wanted spot
    # Get the starting point from the mouse position
    input('Input something when you are ready for the top left corner\n')
    tlx, tly = pyautogui.position()
    print(tlx)
    print(tly)
    # Get the starting point from the mouse position
    input('Input something when you are ready for the bottom right corner\n')
    rbx, rby = pyautogui.position()
    print(rbx)
    print(rby)

    return extract_crop(tlx = tlx, tly = tly, rbx = rbx, rby = rby)

def extract_zillow_address():
    """
    Extract the address from the Zillow website
    based on the user screen size
    :return:
    """
    assert pyautogui.size() == (1920, 1080)
    return extract_crop(tlx=1133
                        , tly=297
                        , rbx=1627
                        , rby=340)


def extract_crop(tlx, tly, rbx, rby):
    """
    Extract a crop
    :param tlx: int x top left position
    :param tly: int y top left position
    :param rbx: int x bottom right position
    :param rby: int y bottom right position
    :return: the crop
    """
    image = pyautogui.screenshot()
    # We change the image color
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    return image[tly:rby, tlx:rbx, :3]  # image[ymin:ymax,xmin:xmax]

def image_to_text(crop):
    """
    transform a image with text into a string
    :param crop : an image
    :return: a string
    """
    text_from_crop = pytesseract.image_to_string(crop)
    return text_from_crop

if __name__ == '__main__':
    #print(pyautogui.size())
    # crop_address = extract_zillow_address()
    crop_address = get_screenshot()
    print(type(crop_address))

    # Plot the crop
    plt.imshow(crop_address)
    plt.title("the address as image")
    plt.show()

    text_from_crop = image_to_text(crop_address)
    print("outupt:" + text_from_crop)