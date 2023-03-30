import unittest
import copy
from ..deployment import Deployment

DUMMY_DEPLOYMENT = {
    "apiVersion": "apps/v1",
    "kind": "Deployment",
    "metadata": {
        "name": "nginx-deployment",
        "labels": {
            "app": "nginx"
        }
    },
    "spec": {
        "replicas": "3",
        "selector": {
            "matchLabels": {
                "app": "nginx"
            }
        },
        "template": {
            "metadata": {
                "labels": {
                    "app": "nginx"
                }
            },
            "spec": {
                "containers": [{
                    "name": "nginx",
                    "image": "nginx:1.14.2",
                    "ports": [{
                        "containerPort": "80"
                    }]
                }]
            }
        }
    }
}

dummyContainers = [{
    "name": "nginx",
    "image": "nginx:1.14.2",
    "ports": [{
        "containerPort": "80"
    }]
}]

class TestDeployment(unittest.TestCase):
    """
    Deployment unit test class
    """
    def setUp(self):
        self.dummy_deployment = Deployment(DUMMY_DEPLOYMENT)


    def test_init(self):
        TEST_DUMMY_DEPLOYMENT = copy.deepcopy(DUMMY_DEPLOYMENT)
        self.assertEqual(self.dummy_deployment, TEST_DUMMY_DEPLOYMENT)

    def test_set_image(self):
        new_image = "nginx:1.15.0-test"
        self.dummy_deployment.set_image(new_image=new_image)
        for c in self.dummy_deployment.get_containers():
            self.assertEqual(new_image, c['image'])

    def test_get_containers(self):
        self.assertEqual(dummyContainers, self.dummy_deployment.get_containers())

    def test_get_updated(self):
        self.assertEqual(self.dummy_deployment.get_updated, DUMMY_DEPLOYMENT)