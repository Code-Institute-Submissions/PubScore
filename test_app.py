# Imports needed
import os
from app import app
import unittest

# Import my env.py that's ignored by git
if os.path.exists("env.py"):
    import env

# Set secret passwords for login tests
SECRET_PASSWORD_ONE = os.environ.get("SECRET_PASSWORD_ONE")
SECRET_PASSWORD_TWO = os.environ.get("SECRET_PASSWORD_TWO")

# Used https://www.youtube.com/watch?v=1aHNs1aEATg for instructions
class FlaskTestCases(unittest.TestCase):

    # Ensure that flask routes where setup correctly

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/index', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_admin(self):
        tester = app.test_client(self)
        tester.post(
            '/login',
            data=dict(username="Frances", password=SECRET_PASSWORD_ONE),
            follow_redirects=True
        )
        response = tester.get('/admin', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_overview(self):
        tester = app.test_client(self)
        response = tester.get('/overview', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_updateteams(self):
        tester = app.test_client(self)
        tester.post(
            '/login',
            data=dict(username="Frances", password=SECRET_PASSWORD_ONE),
            follow_redirects=True
        )
        response = tester.get('/updateteams', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_addteam(self):
        tester = app.test_client(self)
        tester.post(
            '/login',
            data=dict(username="Frances", password=SECRET_PASSWORD_ONE),
            follow_redirects=True
        )
        response = tester.get('/addteam', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_contact(self):
        tester = app.test_client(self)
        tester.post(
            '/login',
            data=dict(username="Frances", password=SECRET_PASSWORD_ONE),
            follow_redirects=True
        )
        response = tester.get('/contact', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the pages load correctly

    def test_index_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/index', content_type='html/text')
        self.assertTrue(b'Welcome to PubScore!' in response.data)

    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Login page!' in response.data)

    def test_admin_page_loads(self):
        tester = app.test_client(self)
        tester.post(
            '/login',
            data=dict(username="Frances", password=SECRET_PASSWORD_ONE),
            follow_redirects=True
        )
        response = tester.get('/admin', content_type='html/text')
        self.assertTrue(b'Welcome to your admin page!' in response.data)

    def test_overview_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/overview', content_type='html/text')
        self.assertTrue(b'Team ranking!' in response.data)

    def test_updateteams_page_loads(self):
        tester = app.test_client(self)
        tester.post(
            '/login',
            data=dict(username="Frances", password=SECRET_PASSWORD_ONE),
            follow_redirects=True
        )
        response = tester.get('/updateteams', content_type='html/text')
        self.assertTrue(b'Update teams!' in response.data)

    def test_addteam_page_loads(self):
        tester = app.test_client(self)
        tester.post(
            '/login',
            data=dict(username="Frances", password=SECRET_PASSWORD_ONE),
            follow_redirects=True
        )
        response = tester.get('/addteam', content_type='html/text')
        self.assertTrue(b'Add a new team!' in response.data)

    def test_contact_page_loads(self):
        tester = app.test_client(self)
        tester.post(
            '/login',
            data=dict(username="Frances", password=SECRET_PASSWORD_ONE),
            follow_redirects=True
        )
        response = tester.get('/contact', content_type='html/text')
        self.assertTrue(b'In case of any problems...' in response.data)

    # Ensure that the login behaves correctly, given the correct credentials

    def test_correct_credentials_1(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username="Frances", password=SECRET_PASSWORD_ONE),
            follow_redirects=True
        )
        self.assertIn(b'Welcome to your admin page!', response.data)

    def test_correct_credentials_2(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username="Admin", password=SECRET_PASSWORD_TWO),
            follow_redirects=True
        )
        self.assertIn(b'Welcome to your admin page!', response.data)

    # Ensure that the login behaves correctly, given the wrong credentails

    def test_wrong_credentials(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username="Admin", password=SECRET_PASSWORD_ONE),
            follow_redirects=True
        )
        self.assertIn(b'Please use the correct username and password',
                      response.data)

    # Ensure logout behaves correctly

    def test_correct_logout(self):
        tester = app.test_client(self)
        tester.post(
            '/login',
            data=dict(username="Frances", password=SECRET_PASSWORD_ONE),
            follow_redirects=True
        )
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b'Welcome to PubScore!', response.data)


if __name__ == "__main__":
    unittest.main()
