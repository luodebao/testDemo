# import selenium
# #import sleep
#import playwright
import pytest

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("password", None)

def test_metadata(metadata):
    assert 'metadata' in metadata['Plugins']
# from selenium import webdriver
# driver = webdriver.Chrome()
#
# driver.get("https://www.google.com/")