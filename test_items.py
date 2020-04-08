import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# pytest --language=es test_items.py
# pytest --language=fr test_items.py

def test_find_button_add_to_cart(browser):
    browser.get(link)
    time.sleep(30) # для проверки 2 критерия
    elem = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert elem != None, "Element not found!"