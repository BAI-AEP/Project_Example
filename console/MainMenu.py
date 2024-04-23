from console.console_base import Menu, MenuOption
from console.SearchMenu import SearchMenu

class MainMenu(Menu):
    def __init__(self):
        super().__init__("Main Menu")
        self.add_option(MenuOption("Search Hotel"))
        self._search_menu = SearchMenu(self)
        self.add_option(MenuOption("Quit"))

    def _navigate(self, choice: int):
        match choice:
            case 1:
                return self._search_menu
            case 2:
                return None