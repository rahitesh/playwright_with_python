from playwright.sync_api import Page

class Login_Page:
    def __init__(self, page:Page):
        self.page = page
        self.new_user_signup_text = page.get_by_text("New User Signup!")
        self.signup_name = page.get_by_role("textbox", name="Name")
        self.signUp_email_Address = page.get_by_role("textbox", name="Email Address")
        self.signUp_Btn = page.get_by_role("button", name="Signup")

        
    def enter_name(self, name):
        self.signup_name.clear()
        self.signup_name.fill(name)

    def enter_email_addr(self, email_addr):
        self.signUp_email_Address.clear()
        self.signUp_email_Address.fill(email_addr)
    
    def click_on_signUp_btn(self):
        self.signUp_Btn.click()
        self.page.wait_for_load_state("domcontentloaded")

    
