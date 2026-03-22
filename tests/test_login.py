from pages.login_page import LoginPage


def test_login(page):
    login = LoginPage(page)
    login.open()
    login.login("aharutyunyan+teacheradmin1@avallain.com", "Anteacheradmin9dev")

    assert "login" not in page.url.lower() or page.locator("[data-testid='user-menu'], .dashboard, nav").count() > 0
