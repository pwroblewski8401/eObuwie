from selenium.webdriver.common.by import By


class MainPageLocators():
    main_page_login_button = (By.XPATH, '//a[@data-testid="header-link-login"]')
    main_page_signin_button = (By.XPATH, '//a[@data-testid="header-register-link"]')
    main_page_cookies_accept_button = (By.XPATH, '//button[@data-testid="permission-popup-accept"]')

class LoginPageLocators():
    login_page_login_button = (By.XPATH, '//button[@data-testid="login-submit-button"]')

class SignInLocators():
    signin_page_name_input = (By.XPATH, '//input[@data-testid="register-first-name-field"]')
    signin_page_last_name_input = (By.XPATH, '//input[@data-testid="register-last-name-field"]')
    signin_page_email_input = (By.XPATH, '//input[@data-testid="register-email-field"]')
    signin_page_password_input = (By.XPATH, '//input[@data-testid="register-password-field"]')
    signin_page_password_confirm_input = (By.XPATH, '//input[@data-testid="register-password-confirmation-field"]')
    signin_page_newsletter_checkbox = (By.XPATH, '//input[@data-testid="register-newsletter-checkbox"]')
    singin_page_statement_checkbox = (By.XPATH, '//input[@data-testid="register-statement-checkbox"]')
    signin_page_create_account_button = (By.XPATH, '//button[@data-testid="register-create-account-button"]')
    signin_page_errors_locator = (By.XPATH, '//span[@class="help-block form-error"]')

class MyAccountLocators():
    myaccount_page_title_div = (By.XPATH, '//div[@class="page-title"]')



