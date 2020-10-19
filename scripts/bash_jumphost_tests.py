from test import BaseTestCase

class BashJumphostTests(BaseTestCase):
    def test_square(self):
        self.assertThat(7 ** 2, Equals(49))