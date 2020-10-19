import fixtures

class HostFixture(fixtures.Fixture):
    def _setUp(self):
        self.testVal = 42
        self.addCleanup(delattr, self, 'testVal')