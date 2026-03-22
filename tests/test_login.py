def test_login(page):
    page.goto("https://default.web-dev1.avallainmagnet.com/")
    page.wait_for_load_state("networkidle")

    page.fill("#login-email", "aharutyunyan+teacheradmin1@avallain.com")
    page.fill("#login-password", "Anteacheradmin9dev")
    page.locator("button[type='submit']").click()

    page.wait_for_timeout(3000)
    # assert login was successful by checking the URL changed or a post-login element exists
    assert "login" not in page.url.lower() or page.locator("[data-testid='user-menu'], .dashboard, nav").count() > 0
