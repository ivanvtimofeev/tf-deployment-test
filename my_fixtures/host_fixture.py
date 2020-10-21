import fixtures
import paramiko
import os
import sys
from testtools.content import text_content,attach_file
import logging

class HostFixture(fixtures.Fixture):
    def _setUp(self):
        
        logger = logging.getLogger(__name__)

        self.hostUser = os.getenv("HOST_USER")
        self.hostKey = os.getenv("HOST_PK")
        self.host = os.getenv("HOST_URL")
        with open(os.path.expanduser('pk.key'),'w') as fd:
            fd.write( self.hostKey )

        if( not self.hostUser or not self.hostKey or not self.host):
            raise AssertionError("ERROR: Need to pass host credentials to  run the tests")


        key = paramiko.RSAKey.from_private_key_file('pk.key')
        self._client = paramiko.SSHClient()
        self._client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.connection = self._client.connect(self.host, username=self.hostUser, key_filename = os.path.expanduser('pk.key'), timeout=5)

        self.addCleanup(delattr, self, 'hostUser')
        self.addCleanup(delattr, self, 'hostKey')
        self.addCleanup(delattr, self, 'host')
        self.addCleanup(self._closeSSHConnection)
    
    def _closeSSHConnection(self):
        self._client.close()

