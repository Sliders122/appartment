#dummy for Git test
#another try
#with stagging area et git add

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium import webdriver

opts = Options()
opts.headless = True
assert opts.headless  # Operating in headless mode
opts.add_argument('--no-sandbox')
opts.add_argument('--disable-dev-shm-usage')
browser = Firefox(options=opts)
res = browser.get("https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-117"
                  ".28203672784423%2C%22east%22%3A-117.19406027215575%2C%22south%22%3A32.7746319816297%2C%22north%22"
                  "%3A32.82405263546272%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B"
                  "%22min%22%3A0%2C%22max%22%3A832043%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3500%7D%2C%22ah"
                  "%22%3A%7B%22value%22%3Atrue%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22"
                  "%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C"
                  "%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B"
                  "%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A14%7D")
browser.page_source
