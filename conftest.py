import pytest
import os
from pytest_html import extras


@pytest.fixture(scope="function")
def browser_context_args(browser_context_args):
    return{**browser_context_args, "record_video_dir":"videos/"}

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    This hook function is called after each test execution.
    It captures a screenshot if the test fails.
    """
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failure") else "w"
        with open("failures", mode) as f:
            if "page" in item.funcargs:
                page = item.funcargs["page"]
                screenshot_path = f"screenshot/{item.name}.png"
                page.screenshot(path=screenshot_path)
                extra = getattr(rep, 'extra', [])
                extra.append(extras.image(screenshot_path))
                rep.extra = extra
                # if hasattr(rep, "extra"):
                #     rep.extra.apppend(extras.image(screenshot_path))
                # else:
                #     rep.extra= [extras.image(screenshot_path)]
                #f.write(f"{rep.nodeid} failed: {screenshot_path}\n")


