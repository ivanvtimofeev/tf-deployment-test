from test import BaseTestCase
from my_fixtures import HostFixture
from testtools.matchers import Equals
from testtools.testcase import attr, WithAttributes
from testtools import TestCase
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class BashJumphostTests(WithAttributes,BaseTestCase):
    def setUp(self):
        logger.info("Sample of logger info")
        self.hostConnection  =  self.useFixture(HostFixture())
        super(BaseTestCase, self).setUp()

    def test_square(self):
        logger.info("Sample of logger info from test")
        self.assertThat(7 ** 2, Equals(49))