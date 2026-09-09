import allure


def assert_with(condition: bool, message: str = "") -> None:
    with allure.step(message):
        assert condition, message
