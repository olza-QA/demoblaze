from playwright.sync_api import sync_playwright, Page, Playwright
import pytest


from components.nav_bar import NavBar
from components.log_in_form import LogInForm
from _pytest.fixtures import SubRequest
import allure

@pytest.fixture
def page(request: SubRequest, playwright:Playwright)-> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(record_video_dir='./videos')
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    yield page
    context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    browser.close()
    allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')
    allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)

@pytest.fixture
def initialize_browser_state(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(record_video_dir='./videos')
    page = context.new_page()

    page.goto("https://www.demoblaze.com")

    nav_bar= NavBar(page)
    log_in_form = LogInForm(page)
    nav_bar.click_login_link()
    log_in_form.fill_form("username115","password115")
    log_in_form.click_log_in()
    nav_bar.check_visible_elements_authorized_user("username115")

    context.storage_state(path="browser-state.json")


@pytest.fixture
def page_with_state(request: SubRequest,playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json",record_video_dir='./videos')
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()

    yield page
    context.tracing.stop(path=f'./tracing/{request.node.name}.zip')
    browser.close()
    allure.attach.file(f'./tracing/{request.node.name}.zip', name='trace', extension='zip')
    allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)
