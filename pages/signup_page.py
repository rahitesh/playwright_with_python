from playwright.sync_api import Page, expect

class Signup_page:

    def __init__(self, page:Page):
        self.page= page
        self.enter_ac_info = page.get_by_text("Enter Account Information")
        self.checbox_for_mr = page.get_by_role("radio", name="Mr.")
        self.checkbox_for_mrs = page.get_by_role("radio", name="Mrs.")
        self.password_textbox = page.get_by_role("textbox", name="Password")
        self.days_dropdown = page.locator("#days")
        self.months_dropdown = page.locator("#months")
        self.years_dropdown = page.locator("#years")
        self.signup_newslater_checkbox = page.get_by_role("checkbox", name="Sign up for our newsletter!")
        self.receive_special_offer_checkbox = page.get_by_role("checkbox", name="Receive special offers from our partners!")
        self.first_name_textbox = page.locator("#first_name")
        self.last_name_textbox = page.locator("#last_name")
        self.company_textbox = page.locator("#company")
        self.address_textbox = page.locator("#address1")
        self.address2_textbox = page.locator("#address2")
        self.country_dropown = page.locator("#country")
        self.state_textbox = page.locator("//*[@name='state']")
        self.city_textbox = page.locator("#city")
        self.zipcode_textbox = page.locator("#zipcode")
        self.mobile_no_textbox = page.locator("#mobile_number")
        self.create_account_btn = page.get_by_role("button", name="Create Account")

    def validate_enter_account_information_text_is_visible(self):
        expect(self.enter_ac_info).to_be_visible()

    def select_appropriate_title(self, title:str):
        if title.lower() == "mrs":
            self.checkbox_for_mrs.click()
        else:
            self.checbox_for_mr.click()
    
    def enter_password(self, password_key:str):
        self.password_textbox.fill(password_key)

    def select_date_of_birth(self, dob):
        date = dob.split("/")
        day, month, year = date

        self.days_dropdown.click()
        self.days_dropdown.select_option(day)
        
        self.months_dropdown.click()
        self.months_dropdown.select_option(month)

        self.years_dropdown.click()
        self.years_dropdown.select_option(year)

    def check_signup_newslater_checkbox(self):
        self.signup_newslater_checkbox.check()
    
    def check_receive_special_offer_checkbox(self):
        self.receive_special_offer_checkbox.check()

    def enter_first_name(self, first_name:str):
        self.first_name_textbox.fill(first_name)

    def enter_last_name(self, last_name:str):
        self.last_name_textbox.fill(last_name)

    def enter_company_name(self, company_name):
        self.company_textbox.fill(company_name)
    
    def enter_address(self,addr):
        self.address_textbox.fill(addr)

    def enter_address_2(self, addr2):
        self.address2_textbox.fill(addr2)
    
    def select_country(self, country_name):
        self.country_dropown.click()
        self.country_dropown.select_option("India")
    
    def enter_state(self, state_name):
        self.state_textbox.fill(state_name)
    
    def enter_city(self, city_name):
        self.city_textbox.fill(city_name)
    
    def enter_zipcode(self, zipcode):
        self.zipcode_textbox.fill(zipcode)
    
    def enter_mobile_no(self, mob_no):
        self.mobile_no_textbox.fill(mob_no)

    def select_country(self, country_name):
        self.country_dropown.click()
        self.page.wait_for_load_state("domcontentloaded")
        self.country_dropown.select_option(country_name)
    
    def click_create_account_btn(self):
        self.create_account_btn.click()


    




    