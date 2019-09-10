

def click_navbar_item(
    id_,
    browser_,
    keys,
    time,
):
    # Click on the navbar toggle element to show the menu items.
    navbar_toggle_button = browser_.find_element_by_class_name(
        'navbar-toggler'
        )
    navbar_toggle_button.send_keys(keys.ENTER)

    time.sleep(1)

    button = browser_.find_element_by_id(id_)
    button.click()
