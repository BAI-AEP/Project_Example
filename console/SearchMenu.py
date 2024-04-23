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

    def _navigate(self, choice: int):
        match choice:
            case 1:  # option 1
                # search all hotels with the search manager
                all_hotels = self._search_manager.get_all_hotels()
                for hotel in all_hotels:
                    print(hotel)
                input("Press Enter to continue...")

                # navigate again to this menu
                return self
            case 2: # option 2
                self.clear()
                name = input("Hotel Name: ")
                hotels_by_name = self._search_manager.get_hotels_by_name(name)
                for hotel in hotels_by_name:
                    print(hotel)
                input("Press Enter to continue...")

                # navigate again to this menu
                return self
            case 3: # option 3
                self.clear()
                stars = input("Hotel Stars: ")
                # TODO: Check if it is number, if not output error and ask again... we have done that
                # TODO: implement the search by stars in the search manager
                # TODO: output the search
                print("Implement this by next week")
                input("Press Enter to continue...")

                # navigate again to this menu
                return self
            case 4: # option 4
                # navigate back to the main menu
                return self._main_menu
