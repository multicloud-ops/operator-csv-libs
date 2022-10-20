import os
import unittest
from ..catalog import Catalog

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

PACKAGE = {
    "schema": "olm.package",
    "name": "etcd",
    "defaultChannel": "alpha"
}

CHANNELS = [{
    "schema": "olm.channel",
    "name": "alpha",
    "package": "etcd",
    "entries": [
        {"name":"etcdoperator-community.v0.6.1"},
        {"name":"etcdoperator-community.v0.9.4", "replaces":"etcdoperator-community.v0.6.1"},
    ]
}]

TEST_CHANNEL = {
    "schema": "olm.channel",
    "name": "testChannel",
    "package": "etcd",
    "entries": []
}

TEST_CHANNEL_WITH_061 = {
    "schema": "olm.channel",
    "name": "testChannel",
    "package": "etcd",
    "entries": [{
        "name": "etcdoperator-community.v0.6.1"
    }]
}

TEST_CHANNEL_ENTRY = {
    "name": "etcdoperator-community.v100",
    "replaces": "etcdoperator-community.v0.9.4",
    "skiprange": "<etcdoperator-community.v100"
}

BUNDLES = [
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

BUNDLE_061 = {
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
}

class TestCatalog(unittest.TestCase):

    def setUp(self):
        self.catalog = Catalog(file=f"{THIS_DIR}/test_files/valid_catalog.json")

    def test_init(self):
        self.assertEqual(self.catalog.package, PACKAGE)
        self.assertEqual(self.catalog.channels, CHANNELS)
        self.assertEqual(self.catalog.bundles, BUNDLES)
        self.assertEqual(self.catalog.indent, 4)

    def test_get_channels(self):
        self.assertEqual(self.catalog.channels, self.catalog.get_channels())
        self.assertEqual(self.catalog.get_channels(), CHANNELS)
    
    def test_get_channels_by_substring(self):
        #Assert the channels equal when providing a substring contained by the channel name
        self.assertEqual(self.catalog.channels, self.catalog.get_channels_by_substring("alph"))
        self.assertEqual(self.catalog.get_channels_by_substring("alph"), CHANNELS)

        #Assert the channels do not equal when providing a substring not contained by the channel name
        self.assertNotEqual(self.catalog.channels, self.catalog.get_channels_by_substring("beta"))
        self.assertNotEqual(self.catalog.get_channels_by_substring("beta"), CHANNELS)
    
    def test_get_bundles(self):
        self.assertEqual(self.catalog.get_bundles(), self.catalog.bundles)
        self.assertEqual(self.catalog.get_bundles(), BUNDLES)
    
    def test_get_bundles_by_substring(self):
        #Assert the bundles equal when providing a substring contained by all the bundle names
        self.assertEqual(self.catalog.get_bundles_by_substring('etcd'), self.catalog.bundles)
        self.assertEqual(self.catalog.get_bundles(), BUNDLES)

        #Assert one bundle is in the response when providing a substring contained only by that one, and that the other is not returned
        self.assertIn(BUNDLE_061, self.catalog.get_bundles_by_substring('v0.6.1'))
        self.assertNotIn(BUNDLE_061, self.catalog.get_bundles_by_substring('v0.9.4'))

    def test_get_default_channel(self):
        self.assertEqual(self.catalog.get_default_channel(), 'alpha')
        self.assertEqual(self.catalog.get_default_channel(), self.catalog.package['defaultChannel'])

    def test_add_channel(self):
        self.catalog.add_channel('testChannel', 'etcd')
        self.assertIn(TEST_CHANNEL, self.catalog.get_channels())

    def test_add_channel_entry(self):
        self.catalog.add_channel_entry(channel='alpha', name='etcdoperator-community.v100', replaces='etcdoperator-community.v0.9.4', skiprange='<etcdoperator-community.v100')
        entries = self.catalog.get_channels()[0]['entries']
        self.assertIn(TEST_CHANNEL_ENTRY, entries)

    def test_set_default_channel(self):
        self.catalog.add_channel('testChannel', 'etcd')
        self.catalog.set_default_channel('testChannel')
        self.assertEqual(self.catalog.get_default_channel(), 'testChannel')
        self.assertEqual(self.catalog.package['defaultChannel'], 'testChannel')

    def test_remove_channel(self):
        self.catalog.add_channel('testChannel', 'etcd')
        self.catalog.add_channel_entry(channel='testChannel', name='etcdoperator-community.v0.6.1')
        self.assertIn(TEST_CHANNEL_WITH_061, self.catalog.get_channels())
        self.assertIn(BUNDLE_061, self.catalog.get_bundles())
        self.catalog.remove_channel('testChannel')
        self.assertNotIn(TEST_CHANNEL_WITH_061, self.catalog.get_channels())
        self.assertIn(BUNDLE_061, self.catalog.get_bundles())

    def test_remove_bundle(self):
        self.catalog.remove_bundle('etcdoperator-community.v0.6.1')
        bundle_names = [ i['name'] for i in self.catalog.get_bundles() ]
        self.assertNotIn('etcdoperator-community.v0.6.1', bundle_names)
