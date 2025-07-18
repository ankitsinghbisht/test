import pytest
pytest.importorskip('apnium')

from utils.driver_setup import create_driver


@pytest.fixture
def driver():
    drv = create_driver()
    yield drv
    drv.quit()


def test_login_screen(driver):
    driver.find_element_by_accessibility_id("Login").click()
    assert driver.find_element_by_accessibility_id("Username") is not None
