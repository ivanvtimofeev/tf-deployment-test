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
        (stdin, stdout, stderr) = hostFixture.execOnHost("pwddddd")
        bash_fails = False
        for line in stdout.readlines():
            logger.info("bash.stdout: line is %s " % line)
        for line in stderr.readlines():
            bash_fails = True
            logger.info("bash.stderr: line is %s " % line)
        self.assertFalse(bash_fails)