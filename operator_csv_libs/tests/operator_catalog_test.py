import os
import unittest
from ..catalog import Catalog, OperatorCatalog

#Make sure the tests run in the specified order
unittest.TestLoader.sortTestMethodsUsing = None

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

CATALOG_1_OPERATOR_NAME = 'etcd1'
CATALOG_2_OPERATOR_NAME = 'etcd2'
CATALOG_3_OPERATOR_NAME = 'etcd'

CATALOG_1_PACKAGE = {
    "schema": "olm.package",
    "name": "etcd1",
    "defaultChannel": "alpha"
}

CATALOG_1_CHANNELS = [{
    "schema": "olm.channel",
    "name": "alpha",
    "package": "etcd1",
    "entries": [
        {"name":"etcdoperator-community.v0.6.1"},
        {"name":"etcdoperator-community.v0.9.4", "replaces":"etcdoperator-community.v0.6.1"},
    ]
}]

CATALOG_1_BUNDLES = [
{
    "schema": "olm.bundle",
    "name": "etcdoperator-community.v0.6.1",
    "package": "etcd1",
    "image": "docker.io/anik120/etcd:latest",
    "properties": [
        {
            "type": "olm.gvk",
            "value": {
                "group": "etcd.database.coreos.com",
                "kind": "EtcdCluster",
                "version": "v1beta2"
            }
        },
        {
            "type": "olm.package",
            "value": {
                "packageName": "etcd1",
                "version": "0.6.1"
            }
        }
    ]
},
{
    "schema": "olm.bundle",
    "name": "etcdoperator-community.v0.9.4",
    "package": "etcd1",
    "image": "docker.io/anik120/etcd:v0.9.4",
    "properties": [
        {
            "type": "olm.gvk",
            "value": {
                "group": "etcd.database.coreos.com",
                "kind": "EtcdCluster",
                "version": "v1beta2"
            }
        },
        {
            "type": "olm.package",
            "value": {
                "packageName": "etcd1",
                "version": "0.9.4"
            }
        }
    ]
}
]

CATALOG_2_PACKAGE = {
    "schema": "olm.package",
    "name": "etcd2",
    "defaultChannel": "alpha"
}

CATALOG_2_CHANNELS = [{
    "schema": "olm.channel",
    "name": "alpha",
    "package": "etcd2",
    "entries": [
        {"name":"etcdoperator-community.v0.6.1"},
        {"name":"etcdoperator-community.v0.9.4", "replaces":"etcdoperator-community.v0.6.1"},
    ]
}]

CATALOG_2_BUNDLES = [
{
    "schema": "olm.bundle",
    "name": "etcdoperator-community.v0.6.1",
    "package": "etcd2",
    "image": "docker.io/anik120/etcd:latest",
    "properties": [
        {
            "type": "olm.gvk",
            "value": {
                "group": "etcd.database.coreos.com",
                "kind": "EtcdCluster",
                "version": "v1beta2"
            }
        },
        {
            "type": "olm.package",
            "value": {
                "packageName": "etcd2",
                "version": "0.6.1"
            }
        }
    ]
},
{
    "schema": "olm.bundle",
    "name": "etcdoperator-community.v0.9.4",
    "package": "etcd2",
    "image": "docker.io/anik120/etcd:v0.9.4",
    "properties": [
        {
            "type": "olm.gvk",
            "value": {
                "group": "etcd.database.coreos.com",
                "kind": "EtcdCluster",
                "version": "v1beta2"
            }
        },
        {
            "type": "olm.package",
            "value": {
                "packageName": "etcd2",
                "version": "0.9.4"
            }
        }
    ]
}
]

CATALOG_3_PACKAGE = {
    "schema": "olm.package",
    "name": "etcd",
    "defaultChannel": "alpha"
}

CATALOG_3_CHANNELS = [{
    "schema": "olm.channel",
    "name": "alpha",
    "package": "etcd",
    "entries": [
        {"name":"etcdoperator-community.v0.6.1"},
        {"name":"etcdoperator-community.v0.9.4", "replaces":"etcdoperator-community.v0.6.1"},
    ]
}]

CATALOG_3_BUNDLES = [
{
    "schema": "olm.bundle",
    "name": "etcdoperator-community.v0.6.1",
    "package": "etcd",
    "image": "docker.io/anik120/etcd:latest",
    "properties": [
        {
            "type": "olm.gvk",
            "value": {
                "group": "etcd.database.coreos.com",
                "kind": "EtcdCluster",
                "version": "v1beta2"
            }
        },
        {
            "type": "olm.package",
            "value": {
                "packageName": "etcd",
                "version": "0.6.1"
            }
        }
    ]
},
{
    "schema": "olm.bundle",
    "name": "etcdoperator-community.v0.9.4",
    "package": "etcd",
    "image": "docker.io/anik120/etcd:v0.9.4",
    "properties": [
        {
            "type": "olm.gvk",
            "value": {
                "group": "etcd.database.coreos.com",
                "kind": "EtcdCluster",
                "version": "v1beta2"
            }
        },
        {
            "type": "olm.package",
            "value": {
                "packageName": "etcd",
                "version": "0.9.4"
            }
        }
    ]
}
]

class TestOperatorCatalog(unittest.TestCase):

    def setUp(self):
        self.operatorcatalog = OperatorCatalog(path=f"{THIS_DIR}/test_files/valid_catalogs")

    def test_init(self):
        #Assert that both catalog 1 and catalog 2 are read in (but not catalog 3 as we will add that in from a file later)
        self.assertEqual(self.operatorcatalog.catalogs[CATALOG_1_OPERATOR_NAME].package, CATALOG_1_PACKAGE)
        self.assertCountEqual(self.operatorcatalog.catalogs[CATALOG_1_OPERATOR_NAME].channels, CATALOG_1_CHANNELS)
        self.assertCountEqual(self.operatorcatalog.catalogs[CATALOG_1_OPERATOR_NAME].bundles, CATALOG_1_BUNDLES)
        self.assertEqual(self.operatorcatalog.catalogs[CATALOG_2_OPERATOR_NAME].package, CATALOG_2_PACKAGE)
        self.assertCountEqual(self.operatorcatalog.catalogs[CATALOG_2_OPERATOR_NAME].channels, CATALOG_2_CHANNELS)
        self.assertCountEqual(self.operatorcatalog.catalogs[CATALOG_2_OPERATOR_NAME].bundles, CATALOG_2_BUNDLES)

    def test_remove_catalog(self):
        #Assert the catalog exists
        self.assertIn(CATALOG_2_OPERATOR_NAME, self.operatorcatalog.catalogs.keys())

        #Remove the catalog
        self.operatorcatalog.remove_catalog(CATALOG_2_OPERATOR_NAME)

        #Assert the catalog no longer exists
        self.assertNotIn(CATALOG_2_OPERATOR_NAME, self.operatorcatalog.catalogs.keys())
    
    def test_add_catalog_from_file(self):
        #Assert the catalog does not exist
        self.assertNotIn(CATALOG_3_OPERATOR_NAME, self.operatorcatalog.catalogs.keys())

        #Add the catalog
        self.operatorcatalog.add_catalog_from_file(f"{THIS_DIR}/test_files/valid_catalog.json")

        #Assert the catalog does exist
        self.assertIn(CATALOG_3_OPERATOR_NAME, self.operatorcatalog.catalogs.keys())

    def test_add_catalog_from_directory(self):
        #Assert the catalog does not exist
        self.assertNotIn(CATALOG_2_OPERATOR_NAME, self.operatorcatalog.catalogs.keys())

        #Add the catalog
        self.operatorcatalog.add_catalog_from_directory(f"{THIS_DIR}/test_files/valid_catalogs/etcd2")

        #Assert the catalog exists
        self.assertIn(CATALOG_2_OPERATOR_NAME, self.operatorcatalog.catalogs.keys())

    def test_get_catalogs(self):
        #Assert all operator names are keys in the response of the get_catalogs function
        self.assertIn(CATALOG_1_OPERATOR_NAME, self.operatorcatalog.get_catalogs().keys())
        self.assertIn(CATALOG_2_OPERATOR_NAME, self.operatorcatalog.get_catalogs().keys())
        self.assertIn(CATALOG_3_OPERATOR_NAME, self.operatorcatalog.get_catalogs().keys())

        #Assert all catalogs equal their respective expected values in the response of the get_catalogs function
        self.assertEqual(self.operatorcatalog.get_catalogs()[CATALOG_1_OPERATOR_NAME].package, CATALOG_1_PACKAGE)
        self.assertCountEqual(self.operatorcatalog.get_catalogs()[CATALOG_1_OPERATOR_NAME].channels, CATALOG_1_CHANNELS)
        self.assertCountEqual(self.operatorcatalog.get_catalogs()[CATALOG_1_OPERATOR_NAME].bundles, CATALOG_1_BUNDLES)
        self.assertEqual(self.operatorcatalog.get_catalogs()[CATALOG_2_OPERATOR_NAME].package, CATALOG_2_PACKAGE)
        self.assertCountEqual(self.operatorcatalog.get_catalogs()[CATALOG_2_OPERATOR_NAME].channels, CATALOG_2_CHANNELS)
        self.assertCountEqual(self.operatorcatalog.get_catalogs()[CATALOG_2_OPERATOR_NAME].bundles, CATALOG_2_BUNDLES)
        self.assertEqual(self.operatorcatalog.get_catalogs()[CATALOG_3_OPERATOR_NAME].package, CATALOG_3_PACKAGE)
        self.assertCountEqual(self.operatorcatalog.get_catalogs()[CATALOG_3_OPERATOR_NAME].channels, CATALOG_3_CHANNELS)
        self.assertCountEqual(self.operatorcatalog.get_catalogs()[CATALOG_3_OPERATOR_NAME].bundles, CATALOG_3_BUNDLES)
    
    def test_get_catalogs_by_substring(self):
        #Assert catalog 1 is a key in the response when searching for catalog 1, but not catalog 2
        self.assertIn(CATALOG_1_OPERATOR_NAME, self.operatorcatalog.get_catalogs_by_substring(CATALOG_1_OPERATOR_NAME).keys())
        self.assertNotIn(CATALOG_2_OPERATOR_NAME, self.operatorcatalog.get_catalogs_by_substring(CATALOG_1_OPERATOR_NAME).keys())

        #Assert all catalogs are keys when searching for the more general catalog 3 substring (etcd)
        self.assertIn(CATALOG_1_OPERATOR_NAME, self.operatorcatalog.get_catalogs_by_substring(CATALOG_3_OPERATOR_NAME).keys())
        self.assertIn(CATALOG_2_OPERATOR_NAME, self.operatorcatalog.get_catalogs_by_substring(CATALOG_3_OPERATOR_NAME).keys())
        self.assertIn(CATALOG_3_OPERATOR_NAME, self.operatorcatalog.get_catalogs_by_substring(CATALOG_3_OPERATOR_NAME).keys())

        #Assert no catalogs are in the response when searching by a substring that exists in none of their names
        self.assertNotIn(CATALOG_1_OPERATOR_NAME, self.operatorcatalog.get_catalogs_by_substring("I am not a substring of any operator name").keys())
        self.assertNotIn(CATALOG_2_OPERATOR_NAME, self.operatorcatalog.get_catalogs_by_substring("I am not a substring of any operator name").keys())
        self.assertNotIn(CATALOG_3_OPERATOR_NAME, self.operatorcatalog.get_catalogs_by_substring("I am not a substring of any operator name").keys())

        #Assert catalog 3 equals its respective expected values in the response of the get_catalogs_by_substring function
        self.assertEqual(self.operatorcatalog.get_catalogs_by_substring(CATALOG_3_OPERATOR_NAME)[CATALOG_3_OPERATOR_NAME].package, CATALOG_3_PACKAGE)
        self.assertCountEqual(self.operatorcatalog.get_catalogs_by_substring(CATALOG_3_OPERATOR_NAME)[CATALOG_3_OPERATOR_NAME].channels, CATALOG_3_CHANNELS)
        self.assertCountEqual(self.operatorcatalog.get_catalogs_by_substring(CATALOG_3_OPERATOR_NAME)[CATALOG_3_OPERATOR_NAME].bundles, CATALOG_3_BUNDLES)
    
    def test_get_catalog(self):
        #Assert catalog 1 equals its respective expected values in the response of the get_catalog function
        self.assertEqual(self.operatorcatalog.get_catalogs(CATALOG_1_OPERATOR_NAME).package, CATALOG_1_PACKAGE)
        self.assertCountEqual(self.operatorcatalog.get_catalogs(CATALOG_1_OPERATOR_NAME).channels, CATALOG_1_CHANNELS)
        self.assertCountEqual(self.operatorcatalog.get_catalogs(CATALOG_1_OPERATOR_NAME).bundles, CATALOG_1_BUNDLES)