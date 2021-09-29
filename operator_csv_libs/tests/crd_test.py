from operator_csv_libs.crd import CustomResourceDefinition
import unittest
import pytest
import copy
import os, yaml

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

DUMMY_CRD = {
    "apiVersion": "apiextensions.k8s.io/v1",
    "kind": "CustomResourceDefinition",
    "metadata": {
        "name": "metadataNameDummy",
        "labels": {
            "name": "metadataLabelNameDummy"
        }
    },
    "spec": {
        "group": "specGroupDummy",
        "versions": [{
            "name": "specGroupVersionDummy", 
            "served": "true",
            "storage": "true",
            "schema": {
                "openAPIV3Schema": {
                    "type": "object",
                    "properties": {
                        "spec": {
                            "type": "object",
                            "properties": {
                                "license": {
                                    "properties": {
                                        "accept": {
                                            "enum": [ "true"],
                                            "type": "boolean"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }],
        "scope": "Namespaced",
        "names": {
            "plural": "dummykinds",
            "singluar": "dummykind",
            "kind": "DummyKind",
            "listKind": "DummyKindList",
            "shortNames": [
                "dk"
            ]
        }
    }
}

class TestCRD(unittest.TestCase):
    def setUp(self):
        self.crdDummy = CustomResourceDefinition(DUMMY_CRD)
        with open(THIS_DIR + '/test_files/valid_crd.yaml', 'r') as stream:
            self.crd_sample = yaml.safe_load(stream)
        self.crdReal = CustomResourceDefinition(self.crd_sample)

    def test_init(self):
        self.assertEqual(self.crdDummy.crd, DUMMY_CRD)
        self.assertEqual(self.crdReal.crd, self.crd_sample)

    def test_get_properties(self):
        for k in self.crdReal.get_properties().keys():
            self.assertIn(k, ['license', 'systemStatus', 'version'])