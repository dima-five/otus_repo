
class Page:

    def __init__(self, location):             # constructor
        self.location = location
        self.new_attr = "NEW_ATTR"

    def open(self):
        print(self.location + " page is opened")


main_page = Page(location="/main")
login_page = Page(location="/login")

main_page.open()
login_page.open()
