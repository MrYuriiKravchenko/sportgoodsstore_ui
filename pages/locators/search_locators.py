from selenium.webdriver.common.by import By

search_field_locator = (By.CSS_SELECTOR, "input[name='q']")
button_locator = (By.XPATH, "//button[text()='Поиск']")
results_found_locator = (By.XPATH, "//a[text()='Кроссовки Bug']")