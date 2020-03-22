from selenium.webdriver.common.by import By


class MainPageLocators:
    main_page_login_button = (By.XPATH, '//a[@data-testid="header-link-login"]')
    main_page_signin_button = (By.XPATH, '//a[@data-testid="header-register-link"]')
    main_page_cookies_accept_button = (By.XPATH, '//button[@data-testid="permission-popup-accept"]')
    main_page_search_input = (By.XPATH, '//div[@class="header-content__search-wrapper"]//input[@data-testid="header-search-input-field"]')

class LoginPageLocators:
    login_page_login_button = (By.XPATH, '//button[@data-testid="login-submit-button"]')
    login_page_email_input = (By.XPATH, '//input[@data-testid="login-input-email"]')
    login_page_password_input = (By.XPATH, '//input[@data-testid="login-input-password"]')
    login_page_submit_button = (By.XPATH, '//button[@data-testid="login-submit-button"]')

class SignInLocators:
    signin_page_name_input = (By.XPATH, '//input[@data-testid="register-first-name-field"]')
    signin_page_last_name_input = (By.XPATH, '//input[@data-testid="register-last-name-field"]')
    signin_page_email_input = (By.XPATH, '//input[@data-testid="register-email-field"]')
    signin_page_password_input = (By.XPATH, '//input[@data-testid="register-password-field"]')
    signin_page_password_confirm_input = (By.XPATH, '//input[@data-testid="register-password-confirmation-field"]')
    signin_page_newsletter_checkbox = (By.XPATH, '//input[@data-testid="register-newsletter-checkbox"]')
    singin_page_statement_checkbox = (By.XPATH, '//input[@data-testid="register-statement-checkbox"]')
    signin_page_create_account_button = (By.XPATH, '//button[@data-testid="register-create-account-button"]')
    signin_page_errors_locator = (By.XPATH, '//span[@class="help-block form-error"]')

class MyAccountLocators:
    myaccount_page_title_div = (By.XPATH, '//div[@class="page-title"]')

class SearchPageLocators:
    search_page_h1 = (By.XPATH, '//h1[@class="search-suggestions__header"]')
    search_page_searched_products = (By.XPATH, '//a[@class="products-list__link"]')
    search_page_searched_product_second_names = (By.XPATH, '//a[@class="products-list__link"]//span[@class="products-list__name-second"]')

class ProductPageLocators:
    product_page_product_link = (By.XPATH, '//li[@class="breadcrumbs__item product"]//a[@class="breadcrumbs__item-link"]')
    product_page_list = (By.XPATH, '//div[@class="product-details"]//ul//li')
    product_page_information_label = (By.XPATH, './/div[@class="label"]')
    product_page_information_data = (By.XPATH, './/div[@class="data"]')
