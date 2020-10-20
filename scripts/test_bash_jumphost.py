from test import BaseTestCase
from my_fixtures import HostFixture
from testtools.matchers import Equals
from testtools.testcase import attr, WithAttributes
from testtools import TestCase
import logging

logger = logging.getLogger(__name__)
logger.level = logging.DEBUG

class BashJumphostTests(WithAttributes,BaseTestCase):
    def setUp(self):
        self.hostConnection  =  self.useFixture(HostFixture())
        super(BaseTestCase, self).setUp()

    def test_square(self):
        logger.info("DDDD from test")
        self.assertThat(7 ** 2, Equals(49))