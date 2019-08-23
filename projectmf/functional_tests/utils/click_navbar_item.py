def click_navbar_item(
    id,
    browser_,
    Keys,
    ):
    # Click on the navbar toggle element to show the menu items.
    navbar_toggle_button = browser_.find_element_by_class_name(
        'navbar-toggler'
        )
    navbar_toggle_button.send_keys(Keys.ENTER)

    button = browser_.find_element_by_id(id)
    button.send_keys(Keys.ENTER)
