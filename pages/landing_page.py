from playwright.sync_api import Page

class Landing_Page:

    def __init__(self, page: Page):
        self.page = page
        self.signUpBtn = page.get_by_text(" Signup / Login")

    def click_on_signUp(self):
        self.page.wait_for_load_state("domcontentloaded")
        self.signUpBtn.click()

    
    