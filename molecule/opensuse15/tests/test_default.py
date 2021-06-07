import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


def test_php_cli(host):
    version = host.run("php --version")

    assert version.succeeded
    assert "7.4" in version.stdout


def test_php_cli_config(host):
    config = host.run("php -i | tr -d ' '").stdout

    assert "opcache.enable=>On=>On" in config
    assert "opcache.enable_cli=>On=>On" in config
    assert "opcache.memory_consumption=>96=>96" in config
    assert "opcache.interned_strings_buffer=>16=>16" in config
    assert "opcache.max_accelerated_files=>4096=>4096" in config
    assert "opcache.max_wasted_percentage=>5=>5" in config
    assert "opcache.validate_timestamps=>On=>On" in config
    assert "opcache.revalidate_path=>Off=>Off" in config
    assert "opcache.revalidate_freq=>2=>2" in config
    assert "opcache.max_file_size=>0=>0" in config
    assert "opcache.blacklist_filename=>novalue=>novalue" in config

    assert "expose_php=>On=>On" in config
    assert "memory_limit=>256M=>256M" in config
