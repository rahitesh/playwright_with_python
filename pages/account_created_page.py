from playwright.sync_api import Page,expect

class Account_Created_Page:
    def __init__(self, page:Page):
        self.page = page
        self.account_created_text = page.get_by_text(text="Account Created!")
        self.continue_btn = page.get_by_role("link", name="Continue")

    def click_on_continue_btn(self):
        self.page.wait_for_load_state("domcontentloaded")
        self.continue_btn.click()
    
    def validate_account_created_is_visible(self):
        expect(self.account_created_text).to_be_visible()