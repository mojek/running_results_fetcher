

from running_results_fetcher.enduhube_page_parser import EnduhubPageParser


def test_creating_page_with_raw_html():
    page = EnduhubPageParser('<html></html>')
    assert page.raw_html == '<html></html>'


def test_extract_race_results_from_raw_html(raw_page_html):
    assert raw_page_html == raw_page_html


def test_race_results_after_parse_page(raw_page_html):
    page = EnduhubPageParser(raw_page_html)
    assert len(page.race_results_dict) == 0
    page.parse_page()
    assert len(page.race_results_dict) == 27


def test_race_results_type(raw_page_html):
    page = EnduhubPageParser(raw_page_html)
    page.parse_page()
    assert type(page.race_results_dict[0]) == dict


def test_race_results_race_name(raw_page_html):
    page = EnduhubPageParser(raw_page_html)
    page.parse_page()
    first_race = page.race_results_dict[0]
    assert first_race['race_name'].strip() == 'V Bieg Niepodległości'


def test_race_results_race_distance(raw_page_html):
    page = EnduhubPageParser(raw_page_html)
    page.parse_page()
    first_race = page.race_results_dict[0]
    assert first_race['distance'] == '10 km'


def test_race_results_race_date(raw_page_html):
    page = EnduhubPageParser(raw_page_html)
    page.parse_page()
    first_race = page.race_results_dict[0]
    assert first_race['race_date'] == '2018-11-10'


def test_race_results_runner_birth(raw_page_html):
    page = EnduhubPageParser(raw_page_html)
    page.parse_page()
    first_race = page.race_results_dict[0]
    assert first_race['runner_birth'] == '80'


def test_race_results_result_of_the_race(raw_page_html):
    page = EnduhubPageParser(raw_page_html)
    page.parse_page()
    first_race = page.race_results_dict[0]
    assert first_race['result_of_the_race'] == '00:39:49'


def test_race_results_result_race_type(raw_page_html):
    page = EnduhubPageParser(raw_page_html)
    page.parse_page()
    first_race = page.race_results_dict[0]
    assert first_race['race_type'] == 'Bieganie'
