### wrongwrong wrgon it's just a test
from unittest import mock
from unittest.mock import patch
from main import start, intro, bedchamber


def test_start(self):
    with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
        start() 