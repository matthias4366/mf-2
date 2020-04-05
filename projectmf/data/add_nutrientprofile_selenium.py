

def add_nutrientprofile_selenium(
    webdriver,
    url_add_data,
    username,
    password,
    click_navbar_item,
    keys,
    time,
    json,
    no_such_element_exception,
):

    """
    During development, from time to time the database will be deleted and
    recreated, and thus its contents will be lost. Sandor clegane is using
    the application for his daily needs and thus loses his saved RawIngredient2,
    FullDayOfEating and Mealplanobjects. The first attempted solution
    consisted of fixtures. However, these proved problematic, as RawIngredient2
    objects added from fixtures would not have the same IDs as the original
    RawIngredient2 objects. Thus, the SpecificIngredient objects in the
    FullDayOfEating objects would reference the WRONG RawIngredient2 object.
    To mitigate this problem, new code was written.

    This part of the new code adds the mealplan.
    """

    browser = webdriver.Firefox()

    browser.get(url_add_data)

    # Log In

    # Click navbar toggle

    navbar_toggle = browser.find_element_by_class_name('navbar-toggler')
    navbar_toggle.click()

    login_menu_option = browser.find_element_by_link_text('Login')
    login_menu_option.click()

    # Find login elements
    username_field = browser.find_element_by_name('username')
    password_field = browser.find_element_by_name('password')

    # Input values into the fields
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Simulate clicking on Log In
    click_navbar_item(
        'id_button_login',
        browser,
        keys,
        time,
    )

    click_navbar_item(
        'id_menu_item_nutrient_profiles',
        browser,
        keys,
        time,
    )

    available_path_nutrient_profile = [
        'nutrient_profile/'
        'nutrient_profiles_from_national_institute_of_health.json',
        'nutrient_profile/nutrient_profile_sandor_clegane.json',
    ]

    # Choose which nutrient profiles to add: either a series of
    # nutrient profiles
    # from the national institute of health, as a preset so users can choose
    # among the preset, or the personal nutrient profile of Sandor Clegane.

    path_nutrient_profile = available_path_nutrient_profile[1]

    time.sleep(10)

    with open(path_nutrient_profile, 'r') as fp:
        nutrient_profile_dict_list = json.load(fp)

    # Add the nutrient profiles.

    for k in range(len(nutrient_profile_dict_list)):

        # See if the nutrient profile already exists. If so, delete it.
        try:
            # nutrient_profile_name = \
            browser.find_element_by_id(
                'paragraph ' + nutrient_profile_dict_list[k]['name'])
            try:
                browser.find_element_by_id(
                    'delete ' + nutrient_profile_dict_list[k]['name']).click()
                browser.find_element_by_id(
                    'confirm_delete').click()
                time.sleep(0.5)
            except no_such_element_exception:
                print('Element not found. Not supposed to happen.')
                break
        except no_such_element_exception:
            pass

        browser.find_element_by_id(
            'id_button_new_nutrient_profile'
        ).click()

        time.sleep(0.1)

        for key, value in nutrient_profile_dict_list[k].items():
            id_from_key = 'id_' + key
            if value is not None:
                browser.find_element_by_id(id_from_key).send_keys(
                    str(value)
                )

        # Simulate clicking the save button
        save_button = browser.find_element_by_id(
            'id_button_save_new_nutrientprofile'
        )
        save_button.click()

        time.sleep(0.5)

    # Tear it down
    time.sleep(10)
    browser.quit()
