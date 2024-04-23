import os
from console.MainMenu import MainMenu
from console.console_base import Application


if __name__ == "__main__":
    # set the environment variable, so managers know where to find the db file
    os.environ['DB_FILE'] = "./data/hotel_reservation.db"

    # create the very first main menu
    main_menu = MainMenu()
    # create the app
    app = Application(main_menu)
    # run the app which starts with the main menu set in the constructor above.
    app.run()
