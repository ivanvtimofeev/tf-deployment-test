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

    def checkCmdOnHost(self,cmd):
        hostFixture = self.useFixture(HostFixture())
        (stdin, stdout, stderr) = hostFixture.execOnHost(cmd)
        bash_fails = False
        for line in stdout.readlines():
            logger.info("bash.stdout: %s " % line)
        for line in stderr.readlines():
            bash_fails = True
            logger.info("bash.stderr: %s " % line)
        self.assertFalse(bash_fails)

    def test_square(self):
        logger = logging.getLogger(__name__ + '.test_square')
        self.checkCmdOnHost("pwd")
