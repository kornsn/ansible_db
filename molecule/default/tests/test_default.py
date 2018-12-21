import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_mongo_is_running_and_enabled(host):
    """Test if MongoDB is running and enabled."""
    mongo = host.service('mongod')
    assert mongo.is_running
    assert mongo.is_enabled


def test_config_file(host):
    """Test if config file contains required line."""
    config_file = host.file('/etc/mongod.conf')
    assert config_file.is_file
    assert config_file.contains('bindIp: 0.0.0.0')


def test_mongo_listens_on_port(host):
    """Test that MongoDB listens required port."""
    assert host.socket('tcp://0.0.0.0:27017').is_listening
