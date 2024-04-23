from console.console_base import Menu, MenuOption
from console.SearchMenu import SearchMenu

class MainMenu(Menu):
    def __init__(self):
        super().__init__("Main Menu")
        self.add_option(MenuOption("Search Hotel")) # option 1
        # we need the search menu to navigate to it
        self._search_menu = SearchMenu(self)
        self.add_option(MenuOption("Quit")) # option 2

    def _navigate(self, choice: int):
        match choice:
            case 1:
                # return the menu for search, therefore display as next the search menu
                return self._search_menu
            case 2:
                # return None, therefore the application knows there is nothing more to run and closes the program
                return None