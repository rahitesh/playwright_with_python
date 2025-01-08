from playwright.sync_api import Page, expect

class Delete_Account_Page:
    def __init__(self, page:Page):
        self.page = page
        self.delete_account_text = page.get_by_text("Account Deleted!")
        self.continue_btn = page.get_by_role("link", name="Continue")
    
    def click_on_continue_btn(self):
        self.continue_btn.click()
    
    def validate_account_deleted_text_is_visible(self):
        self.page.wait_for_load_state("domcontentloaded")
        expect(self.delete_account_text).to_be_visible()