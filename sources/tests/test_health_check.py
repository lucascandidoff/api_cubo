from http import HTTPStatus
from sources.utils.setting import setting
from sources.tests.test_base import TestBase

BASE_URL = '/'


class TestHealthCheck(TestBase):

    def test_health_check(self):
        response = self.application.get(f'{BASE_URL}')
        self.assertEqual(HTTPStatus.OK, response.status_code)
        self.assertIn('code', response.json)
        self.assertEqual(HTTPStatus.OK, response.json.get('code'))
        self.assertIn('data', response.json)
        self.assertIn('application_name', response.json.get('data'))
        self.assertEqual(setting.APPLICATION_NAME, response.json.get('data').get('application_name'))
        self.assertIn('application_version', response.json.get('data'))
        self.assertEqual(setting.APPLICATION_VERSION, response.json.get('data').get('application_version'))
