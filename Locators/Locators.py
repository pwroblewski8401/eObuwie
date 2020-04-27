from selenium.webdriver.common.by import By


class MainPageLocators:
    main_page_login_button = (By.XPATH, '//a[@data-testid="header-link-login"]')
    main_page_signin_button = (By.XPATH, '//a[@data-testid="header-register-link"]')
    main_page_cookies_accept_button = (By.XPATH, '//button[@data-testid="permission-popup-accept"]')
    main_page_search_input = (By.XPATH, '//div[@class="header-content__search-wrapper"]//input[@data-testid="header-search-input-field"]')
    main_page_search_productsFormQuickList = (By.XPATH, '//div[@class="quicksearch__product"]')
    main_page_search_quickList = (By.XPATH, '//div[@class="quicksearch__left"]')
    main_page_search_productsFormQuickListFirstName = (By.XPATH, '//div[@class="quicksearch__product-name-first"]')
    main_page_search_productsFormQuickListSecondName = (By.XPATH, 'a/div[@class="quicksearch__product-name"]/div[@class="quicksearch__product-name-second"]')
    main_page_cookies_close_button = (By.XPATH, '//button[@class="popup__button"]')
    main_page_cart_button =(By.XPATH, '//button[@class="header-cart-button e-button"]')
    main_page_see_cart_button = (By.XPATH, '//div[@class="minicart"]/a[@href="https://www.eobuwie.com.pl/checkout/cart/"]')

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
    product_page_add_to_cart = (By.XPATH, '//button[@data-testid="product-add-to-cart-button"]')
    product_page_search_input = (By.XPATH, '//div[@class="header-content__search-wrapper"]//input[@data-testid="header-search-input-field"]')
    product_page_search_productsFormQuickListSecondName = (By.XPATH, 'a/div[@class="quicksearch__product-name"]/div[@class="quicksearch__product-name-second"]')
    product_page_close_basket_popup_button = (By.XPATH, '//button[@data-testid="product-go-to-cart-close-button"]')
    product_page_size_selector = (By.XPATH, '//div[@data-testid="product-size-select-desktop"]')
    product_page_sizes_ul = (By.XPATH, '//ul[@class="dropdown-menu"]')
    product_page_sizes = (By.XPATH, '//ul[@class="dropdown-menu"]/li')
    product_page_cart_button =(By.XPATH, '//button[@class="header-cart-button e-button"]')
    product_page_availability = (By.XPATH, '//div[@class="product-status__label"]')

class CartPageLocators:
    cart_page_product_in_cart = (By.XPATH, '//div[@class="cart-item__info"]')
    cart_page_product_model_in_cart = (By.XPATH, '//div[@class="cart-item__name-second"]')
