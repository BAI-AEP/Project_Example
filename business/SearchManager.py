import os

from sqlalchemy import select, func

from business.BaseManager import BaseManager
from data_models.models import Hotel


class SearchManager(BaseManager):
    def __init__(self) -> None:
        super().__init__()

    def get_all_hotels(self) -> List[Hotel]:
        query = select(Hotel)
        return self.select_all(query)

    def get_hotels_by_name(self, name: str) -> List[Hotel]:
        query = select(Hotel).where(func.lower(Hotel.name).like(f"%{name.lower()}%"))
        return self.select_all(query)

if __name__ == '__main__':
    # This is only for testing without Application
    # Because we are executing this file in the folder ./business/
    # we need to relatively navigate first one folder up and therefore,
    # use ../data in the path instead of ./data
    os.environ['DB_FILE'] = '../data/test.db'
    search_manager = SearchManager()
    all_hotels = search_manager.get_all_hotels()
    for hotel in all_hotels:
        print(hotel)
