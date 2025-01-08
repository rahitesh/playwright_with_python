import re

from playwright.sync_api import Page, expect
from pages.landing_page import Landing_Page
from pages.login_page import Login_Page
from pages.signup_page import Signup_page
from pages.account_created_page import Account_Created_Page
from pages.delete_account_page import Delete_Account_Page

def test_user_registration_process(page:Page):
    landing_page = Landing_Page(page)
    login_page = Login_Page(page)
    signup_page = Signup_page(page)
    account_created_page = Account_Created_Page(page)
    delete_account_page = Delete_Account_Page(page)

    page.goto("http://automationexercise.com")
    page.wait_for_load_state("domcontentloaded")

    landing_page.click_on_signUp()

    page.wait_for_load_state("domcontentloaded")

    login_page.validate_new_user_signup_text_is_visible()
    login_page.enter_name("Ramesh")
    login_page.enter_email_addr("ramesh11@gmgail.com")
    login_page.click_on_signUp_btn()

    page.wait_for_load_state("domcontentloaded")

    signup_page.validate_enter_account_information_text_is_visible()
    signup_page.select_appropriate_title("Mr")
    signup_page.enter_password("Ramesh@1397")
    signup_page.select_date_of_birth("3/5/2000")
    signup_page.check_signup_newslater_checkbox()
    signup_page.check_receive_special_offer_checkbox()
    signup_page.enter_first_name("Ramesh")
    signup_page.enter_last_name("Tamesh")
    signup_page.enter_company_name("TTTCCCSS")
    signup_page.enter_address("abcd flat street")
    signup_page.enter_address_2("near tamatam road")
    signup_page.select_country("Israel")
    signup_page.enter_state("Lenin")
    signup_page.enter_city("Gaza")
    signup_page.enter_zipcode("6787567")
    signup_page.enter_mobile_no("9876543210")
    signup_page.click_create_account_btn()

    account_created_page.validate_account_created_is_visible()
    account_created_page.click_on_continue_btn()
    page.wait_for_load_state("domcontentloaded")

    loggedIn_user_ele = landing_page.logged_in_user_element()
    expect(loggedIn_user_ele).to_have_text("Ramesh")
    landing_page.click_on_delete_account_link()

    delete_account_page.validate_account_deleted_text_is_visible()
    delete_account_page.click_on_continue_btn()




