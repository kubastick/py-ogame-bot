from selenium import webdriver


class OgameController:
    browser: webdriver = None

    def __init__(self, path_to_webdriver: str):
        self.browser = webdriver.Chrome(executable_path=path_to_webdriver)

    def login(self, login: str, password: str):
        self.browser.get("https://pl.ogame.gameforge.com/")
        # Find a login tab and click it
        login_tab = self.browser.find_element_by_id("ui-id-1")
        login_tab.click()
        # Close cookie alert, who does not like cookies?
        cookies_alert_close = self.browser.find_element_by_id("accept_btn")
        cookies_alert_close.click()
        # Now type that into fields
        del login_tab

        login_field = self.browser.find_element_by_id("usernameLogin")
        login_field.send_keys(login)

        password_field = self.browser.find_element_by_id("passwordLogin")
        password_field.send_keys(password)

        submit_button = self.browser.find_element_by_id("loginSubmit")
        submit_button.click()

        del login_field
        del password_field

    def __del__(self):
        if self.browser is not None:
            self.browser.quit()
