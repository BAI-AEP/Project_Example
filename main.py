import os
from console.MainMenu import MainMenu
from console.console_base import Application


if __name__ == "__main__":
    os.environ['DB_FILE'] = "./data/hotel_reservation.db"
    main_menu = MainMenu()
    app = Application(main_menu)
    app.run()
