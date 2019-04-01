from bs4 import BeautifulSoup
from .race_result import RaceResult


class PageHolder:
    """It' take care of downloaded page"""

    def __init__(self, raw_html):
        self.raw_html = raw_html
        self.race_results = []

    def parse_page(self):
        soup = BeautifulSoup(self.raw_html, 'html.parser')
        for row in soup.find_all('tr', class_='Zawody'):
            event_name = row.find('td', class_='event').get_text()
            race_result = RaceResult(race_name=event_name)
            self.race_results.append(race_result)
