from datetime import datetime

import pytest


@pytest.mark.usefixtures("setup_and_teardown")
class BaseTest:
    # pass
    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return "alex" + time_stamp + "@gmail.com"