from pajaro import __version__
from pajaro.main import pajaro


def test_version():
    assert __version__ == '0.1.0'


def test_default():
    pajaro()


def test_key():
    pajaro(['i'])


def test_keys():
    assert False


def test_interval():
    assert False


def test_key_interval():
    assert False


def test_keys_interval():
    assert False
