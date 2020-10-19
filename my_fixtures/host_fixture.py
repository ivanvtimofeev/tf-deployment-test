import fixtures

class HostFixture(fixtures.Fixture):
    def _setUp(self):
        self.testValue = 49
        self.addCleanup(delattr, self, 'testValue')