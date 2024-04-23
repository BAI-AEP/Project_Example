import os

from console.MainMenu import MainMenu
from console.console_base import Application

DEFAULT_DB = "./data/hotel_reservation.db"

if __name__ == "__main__":
    # if the environment variable is not set, set it to default
    if not os.environ.get('DB_FILE'):
        os.environ['DB_FILE'] = DEFAULT_DB

    # create the very first main menu
    main_menu = MainMenu()
    # create the app
    app = Application(main_menu)
    # run the app which starts with the main menu set in the constructor above.
    app.run()
