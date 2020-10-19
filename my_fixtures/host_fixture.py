import fixtures
import paramiko
import os
from testtools.content import text_content,attach_file

class HostFixture(fixtures.Fixture):
    def _setUp(self):
        self.addDetail('arbitrary-color-name', text_content("blue"))

        self.hostUser = os.getenv("HOST_USER")
        self.hostKey = os.getenv("HOST_PK")
        self.host = os.getenv("HOST_URL")
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        flag = False
        try:
            connaction = client.connect(self.host, username=self.hostUser, pkey=self.hostKey, timeout=5)
        except Exception:
            flag = True
#        client.close()
        self.addCleanup(delattr, self, 'hostUser')
        self.addCleanup(delattr, self, 'hostKey')
        self.addCleanup(delattr, self, 'host')
        self.addDetail('arbitrary-color-name2', text_content(str(connaction)))

