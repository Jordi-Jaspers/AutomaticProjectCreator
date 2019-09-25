import sys
from selenium import webdriver

USERNAME = sys.argv[1]
PASSWORD = sys.argv[2]
REPONAME = sys.argv[3]

browser = webdriver.Chrome()
browser.get('http://github.com/login')

def remove():
    browser.find_elements_by_xpath("//input[@name='login']")[0].send_keys(USERNAME)
    browser.find_elements_by_xpath("//input[@name='password']")[0].send_keys(PASSWORD)
    browser.find_elements_by_xpath("//input[@name='commit']")[0].click()
    browser.get('https://github.com/silv4b/' + REPONAME + '/settings')
    browser.find_elements_by_xpath('//*[@id="options_bucket"]/div[9]/ul/li[4]/details/summary')[0].click()
    browser.find_elements_by_xpath(
        '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/p/input')[0].send_keys(REPONAME)
    browser.find_elements_by_xpath(
        '//*[@id="options_bucket"]/div[9]/ul/li[4]/details/details-dialog/div[3]/form/button')[0].click()
    browser.get("https://github.com/" + USERNAME)


if __name__ == "__main__":
    remove()