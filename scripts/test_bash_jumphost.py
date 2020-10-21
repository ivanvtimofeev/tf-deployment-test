from test import BaseTestCase
from my_fixtures import HostFixture
from testtools.matchers import Equals
from testtools.testcase import attr, WithAttributes
from testtools import TestCase
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BashJumphostTests(WithAttributes,BaseTestCase):
    def setUp(self):
        super(BaseTestCase, self).setUp()

    def test_square(self):
        logger = logging.getLogger(__name__ + '.test_square')
        hostFixture = self.useFixture(HostFixture())
        (stdin, stdout, stderr) = hostFixture.execOnHost("pwd")
        for line in stdout.readlines():
            logger.info("DDDD: line is %s " % line)

        self.assertThat(7 ** 2, Equals(49))