from business.SearchManager import SearchManager
from console.console_base import Menu, MenuOption


class SearchMenu(Menu):
    def __init__(self, main_menu: Menu):
        super().__init__("Search Hotel")
        self.add_option(MenuOption("Show all hotel"))  # option 1
        self.add_option(MenuOption("Search by city"))  # option 2
        self.add_option(MenuOption("Search by stars"))  # option 3
        # TODO: Add further MenuOptions to search by the address.city etc. of the hotels.
        self.add_option(MenuOption("Back"))  # option 4
        # we need the main menu to navigate back to it
        self.__main_menu = main_menu

        self.__search_manager = SearchManager()

    def __show_all(self):
        self.clear() # clear the console
        all_hotels = self.__search_manager.get_all_hotels()  # search all hotels with the search manager
        for hotel in all_hotels:
            print(hotel)
        input("Press Enter to continue...")

    def __search_by_city(self):
        self.clear() # clear the console
        city = input("City: ")
        hotels_by_name = self.__search_manager.get_hotels_by_city(city)  # search by name with the search manager
        for hotel in hotels_by_name:
            print(hotel)
        input("Press Enter to continue...")

    def __search_by_stars(self):
        self.clear() # clear the console
        stars = input("Hotel Stars: ")
        # TODO: Check if it is a number 1-5, if not output error and ask again... we have done that
        # TODO: implement the search by stars in the search manager and call the method
        # TODO: output the search result
        print("Implement this by next week")
        input("Press Enter to continue...")

    # TODO: Add more methods which implement the UI for further search options.

    def _navigate(self, choice: int):
        match choice:
            case 1:  # option 1 (Show all hotel)
                self.__show_all()
                return self  # navigate again to this menu
            case 2:  # option 2 (Search by name)
                self.__search_by_city()
                return self  # navigate again to this menu
            case 3:  # option 3 (Search by starts)
                self.__search_by_stars()
                return self  # navigate again to this menu
            # TODO: Add further navigation options according to the added MenuOptions in the constructor.
            case 4:  # option 4 (Back)
                return self.__main_menu  # navigate back to the main menu
