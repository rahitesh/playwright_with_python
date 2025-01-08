from playwright.sync_api import Page

class Landing_Page:

    def __init__(self, page: Page):
        self.page = page
        self.signUpBtn = page.get_by_text(" Signup / Login")
        self.logged_in_as = page.locator("//*[contains(text(), ' Logged in as ')]/b")
        self.delete_account_link = page.get_by_text(" Delete Account")

    def click_on_signUp(self):
        self.page.wait_for_load_state("domcontentloaded")
        self.signUpBtn.click()
    
    def logged_in_user_element(self):
        return self.logged_in_as
    
    def click_on_delete_account_link(self):
        self.delete_account_link.click()

    
    