from bs4 import BeautifulSoup


class EnduhubPageParser:
    """It' take care of downloaded page"""

    def __init__(self, raw_html):
        self.raw_html = raw_html
        self.race_results_dict = []

    def parse_page(self):
        soup = BeautifulSoup(self.raw_html, 'html.parser')
        for row in soup.find_all('tr', class_='Zawody'):
            event_name = row.find('td', class_='event').get_text()
            distance = row.find('td', class_='distance').get_text()
            race_date = row.find('td', class_='date').get_text()
            runner_birth = row.find('td', class_='yob').get_text()
            result_of_the_race = row.find('td', class_='best').get_text()
            race_type = row.find('td', class_='sport').get_text()
            race_result = dict(
                race_name=event_name,
                distance=distance,
                race_date=race_date,
                runner_birth=runner_birth,
                result_of_the_race=result_of_the_race,
                race_type=race_type)

            self.race_results_dict.append(race_result)
        return self.race_results_dict
