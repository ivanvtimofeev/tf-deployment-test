from test import BaseTestCase
from my_fixtures import HostFixture
from testtools.matchers import Equals
from testtools.testcase import attr, WithAttributes
from testtools import TestCase
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BashJumphostTests(WithAttributes,BaseTestCase):

    def test_square(self):
        logger = logging.getLogger(__name__ + '.test_square')
        self.check_cmd_on_host("pwd")
    
    def test_1(self)
        logger = logging.getLogger(__name__ + '.test1')
        self.run_bash_test_on_host('test1.sh')

    def test_2(self)
        logger = logging.getLogger(__name__ + '.test2')
        self.run_bash_test_on_host('test2.sh')

