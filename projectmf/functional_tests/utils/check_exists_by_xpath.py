

def check_exists_by_xpath(
    webdriver,
    xpath,
    no_such_element_exception,
):
    try:
        webdriver.find_element_by_xpath(xpath)
    except no_such_element_exception:
        return False
    return True
