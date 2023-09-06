import time
from playwright.sync_api import Page, expect
from playwright.sync_api import Page


class ProductPurchasePage:
    def __init__(self, page):
        self.page = page
        self.url = "http://automationexercise.com"
        self.category_text = page.locator("//h2[normalize-space()='Category']")
        self.add_to_cart_button = page.locator("//body[1]/section[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/a[1]")
        self.hover_add_to_cart_button = page.locator("//body[1]/section[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/a[1]")
        self.view_cart = page.locator("//u[normalize-space()='View Cart']")
        self.proceed_to_checkout = page.locator(".btn.btn-default.check_out")
        self.login_register_button = page.locator("//u[normalize-space()='Register / Login']")
        self.sign_up_name = page.locator("//input[@placeholder='Name']")
        self.sign_up_email = page.locator("//input[@data-qa='signup-email']")
        self.sign_up_button = page.locator("//button[normalize-space()='Signup']")
        self.mr_radio_button = page.locator("//input[@id='id_gender1']")
        self.registration_password = page.locator("//input[@id='password']")
        self.day_dropdown = page.locator("//select[@id='days']")
        self.month_dropdown = page.locator("//select[@id='months']")
        self.year_dropdown = page.locator("//select[@id='years']")
        self.registration_first_name = page.locator("//input[@id='first_name']")
        self.registration_last_name = page.locator("//input[@id='last_name']")
        self.registration_company = page.locator("//input[@id='company']")
        self.registration_address = page.locator("//input[@id='address1']")
        self.registration_country = page.locator("//select[@id='country']")
        self.registration_state = page.locator("//input[@id='state']")
        self.registration_city = page.locator("//input[@id='city']")
        self.registration_zipcode = page.locator("//input[@id='zipcode']")
        self.registration_mobile = page.locator("//input[@id='mobile_number']")
        self.registration_create_button = page.locator("//button[contains(text(),'Create Account')]")
        self.registration_continue_button = page.locator("//a[contains(text(),'Continue')]")
        self.top_name = page.locator("div.header-middle div.container div.row div.col-sm-8 div.shop-menu.pull-right ul.nav.navbar-nav li:nth-child(10) a:nth-child(1) > b:nth-child(2)")
        self.home_cart = page.locator("//header/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]")
        self.cart_proceed_to_checkout = page.locator("//a[contains(text(),'Proceed To Checkout')]")
        self.product_name = page.locator("//a[contains(text(),'Blue Top')]")
        self.quantity = page.locator("div.container div.table-responsive.cart_info:nth-child(3) table.table.table-condensed:nth-child(1) tbody:nth-child(2) tr:nth-child(1) td.cart_quantity > button.disabled")
        self.price = page.locator("div.container div.table-responsive.cart_info:nth-child(3) table.table.table-condensed:nth-child(1) tbody:nth-child(2) tr:nth-child(1) td.cart_total > p.cart_total_price")
        self.checkout_quantity = page.locator("div.container div.table-responsive.cart_info:nth-child(5) table.table.table-condensed tbody:nth-child(2) tr:nth-child(1) td.cart_quantity > button.disabled")
        self.checkout_price = page.locator("div.container div.table-responsive.cart_info:nth-child(5) table.table.table-condensed tbody:nth-child(2) tr:nth-child(1) td.cart_total > p.cart_total_price")
        self.click_place_order = page.locator("//a[contains(text(),'Place Order')]")
        self.checkout_comment = page.locator("//body/section[@id='cart_items']/div[1]/div[6]/textarea[1]")
        self.payment_card_name = page.locator("//body/section[@id='cart_items']/div[1]/div[3]/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]")
        self.payment_card_number = page.locator("//body/section[@id='cart_items']/div[1]/div[3]/div[1]/div[2]/form[1]/div[2]/div[1]/input[1]")
        self.payment_card_CVC = page.locator("//body/section[@id='cart_items']/div[1]/div[3]/div[1]/div[2]/form[1]/div[3]/div[1]/input[1]")
        self.payment_card_exp_month = page.locator("//body/section[@id='cart_items']/div[1]/div[3]/div[1]/div[2]/form[1]/div[3]/div[2]/input[1]")
        self.payment_card_exp_year = page.locator("//body/section[@id='cart_items']/div[1]/div[3]/div[1]/div[2]/form[1]/div[3]/div[3]/input[1]")
        self.place_order_and_confrim = page.locator("//button[@id='submit']")
        self.order_confirmation_message = page.locator("//p[contains(text(),'Congratulations! Your order has been confirmed!')]")





    def product_purchase(self, page: Page):
        self.page.goto(self.url)
        time.sleep(2)
        actual_category_text = self.category_text.text_content()
        time.sleep(1)
        expected_category_text = "Category"
        assert actual_category_text == expected_category_text, f"Expected '{expected_category_text}', but got '{actual_category_text}'"
        time.sleep(2)

        page.evaluate("window.scrollTo(0, 800);")
        time.sleep(2)

        self.add_to_cart_button.hover()
        time.sleep(2)
        self.hover_add_to_cart_button.click()
        time.sleep(2)
        self.view_cart.click()

        actual_proceed_to_checkout_text = self.proceed_to_checkout.text_content()
        time.sleep(1)
        expected_proceed_to_checkout_text = "Proceed To Checkout"
        assert actual_proceed_to_checkout_text == expected_proceed_to_checkout_text, f"Expected '{expected_proceed_to_checkout_text}', but got '{actual_proceed_to_checkout_text}'"
        time.sleep(2)

        self.proceed_to_checkout.click()
        time.sleep(2)
        self.login_register_button.click()
        time.sleep(2)

        self.sign_up_name.type("Zahid")
        time.sleep(2)
        self.sign_up_email.type("jevobol708@searpen.com")
        time.sleep(2)
        self.sign_up_button.click()
        time.sleep(2)

        self.mr_radio_button.click()
        time.sleep(2)
        self.registration_password.type("1234qwer")
        time.sleep(2)

        page.evaluate("window.scrollTo(0, 600);")
        time.sleep(2)

        self.day_dropdown.select_option(value="4")
        time.sleep(1)
        self.month_dropdown.select_option(value="7")
        time.sleep(1)
        self.year_dropdown.select_option(value="1996")
        time.sleep(1)

        self.registration_first_name.type("Zahid")
        self.registration_last_name.type("Hasan")
        self.registration_company.type("Kinetik")
        self.registration_address.type("NY, USA")
        self.registration_country.select_option(value = "United States")

        page.evaluate("window.scrollTo(600, 1100);")
        time.sleep(2)

        self.registration_state.type("NY")
        self.registration_city.type("NY")
        self.registration_zipcode.type("1216")
        self.registration_mobile.type("012163433")
        self.registration_create_button.click()
        time.sleep(3)
        self.registration_continue_button.click()

        actual_top_name = self.top_name.text_content()
        expected_name = "Zahid"
        assert actual_top_name == expected_name, f"Expected '{expected_name}', but got '{actual_top_name}'"
        time.sleep(30)

        self.home_cart.click()
        time.sleep(2)
        expected_product_name = self.product_name.text_content()
        expected_product_quantity = self.quantity.text_content()
        expected_product_price = self.price.text_content()
        self.cart_proceed_to_checkout.click()
        time.sleep(1)

        actual_product_name= self.product_name.text_content()
        actual_product_quantity = self.checkout_quantity.text_content()
        actual_product_price = self.checkout_price.text_content()
        assert actual_product_name == expected_product_name, f"Expected '{expected_product_name}', but got '{actual_product_name}'"
        time.sleep(1)
        assert actual_product_quantity == expected_product_quantity, f"Expected '{expected_product_quantity}', but got '{actual_product_quantity}'"
        time.sleep(1)
        assert actual_product_price == expected_product_price, f"Expected '{expected_product_price}', but got '{actual_product_price}'"
        time.sleep(1)

        page.evaluate("window.scrollTo(0, 600);")
        time.sleep(2)

        self.checkout_comment.type("Delivery 7pm - 10pm")
        self.click_place_order.click()

        self.payment_card_name.type("Zahid hasan")
        self.payment_card_number.type("4111111111111111")
        self.payment_card_CVC.type("245")
        self.payment_card_exp_month.type("12")
        self.payment_card_exp_year.type("25")
        time.sleep(2)
        self.place_order_and_confrim.click()
        time.sleep(3)
        Actual_confirm_message = self.order_confirmation_message.text_content()
        Expected_confirm_message = "Congratulations! Your order has been confirmed!"
        assert Actual_confirm_message == Expected_confirm_message, f"Expected '{Expected_confirm_message}', but got '{Actual_confirm_message}'"
        time.sleep(1)
