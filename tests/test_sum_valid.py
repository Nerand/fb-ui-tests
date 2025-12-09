from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def go_to_sum_input(driver, base_url):
    driver.get(base_url)
    cards = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".g-card"))
    )
    cards[0].click()

    card_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[placeholder='0000 0000 0000 0000']"))
    )
    card_input.send_keys("1" * 16)

    return WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH,
             "//h3[text()='Сумма перевода:']/following-sibling::input[1]")
        )
    )


def test_not_accept_sum(driver, base_url):
    field = go_to_sum_input(driver, base_url)
    field.clear()
    field.send_keys("9099")

    button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button.g-button"))
    )
    assert button.is_enabled(), "Перевод отклоняется при валидной сумме"


def test_input_summ_negative(driver, base_url):
    field = go_to_sum_input(driver, base_url)
    field.clear()
    field.send_keys("-10")

    value = field.get_attribute("value")
    assert "-" not in value, "Можно ввести отрицательную сумму"


def test_empty_sum(driver, base_url):
    field = go_to_sum_input(driver, base_url)
    field.clear()

    button = driver.find_elements(By.CSS_SELECTOR, "button.g-button")
    assert len(button) == 0, "Кнопка «Перевести» появляется при пустой сумме"
