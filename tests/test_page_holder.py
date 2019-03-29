from running_results_fetcher.page_holder import PageHolder
from running_results_fetcher.race_result import RaceResult


def test_creating_page_with_raw_html():
    page = PageHolder('<html></html>')
    assert page.raw_html == '<html></html>'


def test_extract_race_results_from_raw_html(raw_page_html):
    assert raw_page_html == raw_page_html


def test_parse_page(raw_page_html):
    page = PageHolder(raw_page_html)
    assert page.parse_page() == None


def test_race_results_after_parse_page(raw_page_html):
    page = PageHolder(raw_page_html)
    assert len(page.race_results) == 0
    page.parse_page()
    assert len(page.race_results) == 27


def test_race_results_type(raw_page_html):
    page = PageHolder(raw_page_html)
    page.parse_page()
    assert type(page.race_results[0]) == RaceResult


def test_race_results_race_name(raw_page_html):
    page = PageHolder(raw_page_html)
    page.parse_page()
    first_race = page.race_results[0]
    assert first_race.race_name == 'V Bieg Niepodległości'


# def test_race_results_race_name(raw_page_html):
#     page = PageHolder(raw_page_html)
#     page.parse_page()
#     first_race = page.race_results[0]
#     assert first_race.distance == 10
