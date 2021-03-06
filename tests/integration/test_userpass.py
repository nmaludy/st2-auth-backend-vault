import mock
import os
import unittest

from base import BaseIntegrationTestCase


class TestVaultUserPass(BaseIntegrationTestCase):

    def setUp(self):
        super(TestVaultUserPass, self).setUp()
        client = self.create_client()
        client.sys.enable_auth_method('userpass')

    def tearDown(self):
        super(TestVaultUserPass, self).tearDown()
        client = self.create_client()
        client.sys.disable_auth_method('userpass')

    def test_userpass_good(self):
        client = self.create_client()
        client.write('auth/userpass/users/testuser',
                     password="xxx")
        backend = self.create_backend('userpass')

        result = backend.authenticate('testuser', 'xxx')
        self.assertEquals(result, True)

    def test_userpass_fail(self):
        backend = self.create_backend('userpass')
        result = backend.authenticate('junkuser', 'badpassword')
        self.assertEquals(result, False)
