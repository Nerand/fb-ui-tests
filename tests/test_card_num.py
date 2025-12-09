from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def open_first_account(driver):
    cards = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".g-card"))
    )
    cards[0].click()


def test_num_lim_len(driver, base_url):
    driver.get(base_url)
    open_first_account(driver)

    card_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[placeholder='0000 0000 0000 0000']")
        )
    )

    card_input.send_keys("1" * 20)
    value = card_input.get_attribute("value").replace(" ", "")

    assert len(value) <= 16, "Поле принимает > 16 символов"
