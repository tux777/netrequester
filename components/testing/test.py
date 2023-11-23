import json, sys
from components.logging.logging import logger

settings = {}

def startTest(testName, testSettings, generalSettings):
    match testName:        
        case 'get':
            from components.testing.testing_segments.test_get import test
            test()
        case 'option':
            from components.testing.testing_segments.test_option import test
            test()
        case 'post':
            from components.testing.testing_segments.test_post import test
            test()

def test():
    with open('./config/testing.json', 'r') as config:
        settings = json.load(config)

    # Test Settings Handler
    for test in settings:
        if isinstance(settings[test], dict):
            if test != "general":
                test_logger = logger(None) # No default logger type
                log_count = 0
                test_logger.attachCounter(log_count)
                log_count += 1
                test_logger.log(test_logger.counts)

                if settings[test].get("enabled"):
                    test_settings = {}
                    for test_setting in settings[test]:
                        test_settings.update({f'{test_setting}': f'{settings[test].get(test_setting)}'})

                    test_logger.log(f"Starting {test} test.", "info")
                    try:
                        startTest(test, test_settings, settings.get("general"))
                    except AssertionError as err:
                        test_logger.log(f"{err}", "error")
                else:
                    test_logger.log(f"{test.capitalize()} test is disabled, continuing...", "warning")
            else:
                continue
        else:
            continue