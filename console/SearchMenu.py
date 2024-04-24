from business.SearchManager import SearchManager
from console.console_base import Menu, MenuOption


class SearchMenu(Menu):
    def __init__(self, main_menu: Menu):
        super().__init__("Search Hotel")
        self.add_option(MenuOption("Show all hotel"))  # option 1
        self.add_option(MenuOption("Search by name"))  # option 2
        self.add_option(MenuOption("Search by stars"))  # option 3
        self.add_option(MenuOption("Back"))  # option 4
        # we need the main menu to navigate back to it
        self._main_menu = main_menu

        self._search_manager = SearchManager()

    def __search_all(self):
        self.clear()
        all_hotels = self._search_manager.get_all_hotels()  # search all hotels with the search manager
        for hotel in all_hotels:
            print(hotel)
        input("Press Enter to continue...")

    def __search_by_name(self):
        self.clear()
        name = input("Hotel Name: ")
        hotels_by_name = self._search_manager.get_hotels_by_name(name)  # search by name with the search manager
        for hotel in hotels_by_name:
            print(hotel)
        input("Press Enter to continue...")

    def __search_by_stars(self):
        self.clear()
        stars = input("Hotel Stars: ")
        # TODO: Check if it is a number 1-5, if not output error and ask again... we have done that
        # TODO: implement the search by stars in the search manager and call the method
        # TODO: output the search result
        print("Implement this by next week")
        input("Press Enter to continue...")

    def _navigate(self, choice: int):
        match choice:
            case 1:  # option 1
                self.__search_all()  # navigate again to this menu
                return self
            case 2:  # option 2
                self.__search_by_name()
                return self  # navigate again to this menu
            case 3:  # option 3
                self.__search_by_stars()
                return self  # navigate again to this menu
            case 4:  # option 4
                return self._main_menu  # navigate back to the main menu
