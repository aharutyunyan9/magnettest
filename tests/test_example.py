from pages.base_page import BasePage


def test_page_title(page):
    base = BasePage(page)
    base.navigate("https://default.web-dev1.avallainmagnet.com/")
    assert base.get_title()
