import fixtures
import paramiko
import os
import sys
from testtools.content import text_content,attach_file

import logging
logger = logging.getLogger()
logger.level = logging.DEBUG

class HostFixture(fixtures.Fixture):
    def _setUp(self):
        self.hostUser = os.getenv("HOST_USER")
        self.hostKey = os.getenv("HOST_PK")
        self.host = os.getenv("HOST_URL")

        stream_handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(stream_handler)
        logging.getLogger().debug(u"DDDDD")

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
    

