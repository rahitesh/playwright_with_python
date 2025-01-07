from playwright.sync_api import Page

class Signup_page:

    def __init__(self, page:Page):
        self.page= page
        self.enter_ac_info = page.get_by_text("Enter Account Information")
        self.checbox_for_mr = page.get_by_role("radio", name="Mr.")
        self.checkbox_for_mrs = page.get_by_role("radio", name="Mrs.")
        self.enter_password = page.get_by_role("textbox", "Password")
        self.days_dropdown = page.locator(id="days")
        self.months_dropdown = page.locator(id="months")
        self.years_dropdown = page.locator(id="years")


    def select_appropriate_title(self, title:str):
        if title.lower() == "mrs":
            self.checkbox_for_mrs.click()
        else:
            self.checbox_for_mr.click()

    def select_date_of_birth(self, dob):
        date = dob.split(",")
        day, month, year = date

        self.days_dropdown.click()
        self.days_dropdown.select_option(day)
        
        self.months_dropdown.click()
        self.months_dropdown.select_option(month)

        self.years_dropdown.click()
        self.years_dropdown.select_option(year)




    