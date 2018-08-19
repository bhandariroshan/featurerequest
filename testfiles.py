import os
import unittest
import tempfile
from settings import app


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    def test_empty_db(self):
        rv = self.app.get('/')
        print(rv.data)
        assert b'No entries here so far' in rv.data


if __name__ == '__main__':
    unittest.main()