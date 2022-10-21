
class ChromeBrowser:

    def __repr__(self):  # If need to present as 'Chrome' name after invoking current class
        return "Chrome"


class Page:

    def __init__(self, browser, location):
        self.browser = browser
        self.location = location

    def open(self):
        print(self.location + " page is opened in " + str(self.browser))


class MainPage(Page):
    pass


class LoginPage(Page):

    def login(self, username, password):
        print(f"logged in with: {username} and {password}")


browser = ChromeBrowser()
main_page = MainPage(browser=browser, location="/main")
login_page = LoginPage(browser=browser, location="/login")

main_page.open()
login_page.open()
login_page.login('admin', 'qwerty')
