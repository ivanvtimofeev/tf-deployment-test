import fixtures
import paramiko
import os

class HostFixture(fixtures.Fixture):
    def _setUp(self):
        self.hostUser = os.getenv("HOST_USER")
        self.hostKey = os.getenv("HOST_PK")
        self.host = os.getenv("HOST_URL")
        self.addCleanup(delattr, self, 'hostUser')
        self.addCleanup(delattr, self, 'hostKey')
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(self.host, username=self.hostUser, pkey=self.hostKey, timeout=5)
        client.close()

