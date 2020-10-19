from test import BaseTestCase
from my_fixtures import HostFixture
from testtools.matchers import Equals
from testtools.testcase import attr, WithAttributes
from testtools import TestCase

class BashJumphostTests(WithAttributes,BaseTestCase):
    def test_square(self):
        fixture = self.useFixture(HostFixture())
        self.assertThat(7 ** 2, Equals(fixture.testValue))