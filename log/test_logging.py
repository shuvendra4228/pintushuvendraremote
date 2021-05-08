import pytest
from log.baseClassLog import BaseClass


class Testexample(BaseClass):
    def test_tc001(self):
        log = self.getlogger()
        log.info("hi info")
        log.warning("hi warning")
