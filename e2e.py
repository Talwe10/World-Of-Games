from selenium import webdriver
from selenium.webdriver.common.by import By


my_driver = webdriver.Chrome(executable_path=r'/Users/tal.weinstein/Downloads/chromedriver 103v')


def test_scores_service():
    my_driver.get('http://127.0.0.1:5000')
    score = int(my_driver.find_element(By.XPATH, '//*[@id="score"]').text)

    if 1000 >= score >= 1:
        return True
    else:
        return False


# The main_function will return -1 as an OS exit code if the tests failed and 0 if they passed.
def main_function():
    test = test_scores_service()
    if test is True:
        print("The word 'score' is found, that means it's working")
        return 0

    else:
        print("-1")
        return -1


main_function()
