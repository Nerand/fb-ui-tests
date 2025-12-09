from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def open_rub_and_card(driver, base_url):
    driver.get(base_url)
    cards = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".g-card"))
    )
    cards[0].click()

    return WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[placeholder='0000 0000 0000 0000']"))
    )


def test_comission_rub_negative(driver, base_url):
    card = open_rub_and_card(driver, base_url)
    card.send_keys("1" * 16)

    sum_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH,
             "//h3[text()='Сумма перевода:']/following-sibling::input[1]")
        )
    )
    sum_input.clear()
    sum_input.send_keys("9099")

    commission = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#comission"))
    )

    assert commission.text == "909", "Комиссия неправильно вычислена"
