import fixtures
import paramiko
import os
import sys
from testtools.content import text_content,attach_file
import logging

class HostFixture(fixtures.Fixture):
    def _setUp(self):
        self.hostUser = os.getenv("HOST_USER")
        self.hostKey = os.getenv("HOST_PK")
        self.host = os.getenv("HOST_URL")

        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger(__name__)
        logger.level = logging.DEBUG
        logger.warning(u"DDDDD2 warnig")
        logger.debug(u"DDDDD3 debug")

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        flag = False
        connection = ""
        try:
            connection = client.connect(self.host, username=self.hostUser, pkey=self.hostKey, timeout=5)
        except Exception as e:
            self.addDetail('error', text_content(str(e)))
            flag = True
        client.close()
        self.addCleanup(delattr, self, 'hostUser')
        self.addCleanup(delattr, self, 'hostKey')
        self.addCleanup(delattr, self, 'host')
    

