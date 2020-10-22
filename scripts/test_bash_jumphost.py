from deployment_test import BaseTestCase
from testtools.testcase import attr, WithAttributes
import logging

logging.basicConfig(level=logging.INFO)

class BashJumphostTests(WithAttributes,BaseTestCase):
    def test_1(self):
        logger = logging.getLogger(__name__ + '.test1')
        self.run_bash_test_on_host('test1.sh',logger)

    def test_2(self):
        logger = logging.getLogger(__name__ + '.test2')
        self.run_bash_test_on_host('test2.sh',logger)

    @attr(["orchestrator_k8s","deployer_manifests"])
    def test_manifests_k8s_smoke(self):
        logger = logging.getLogger(__name__ + '.manifests_k8s_smoke')
        self.run_bash_test_on_host('k8s_manifests_k8s.sh',logger)