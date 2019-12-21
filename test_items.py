import time


def test_add_to_cart_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    browser.get(link)

    btn = browser.find_element_by_css_selector('.btn-add-to-basket')

    assert btn is not None

