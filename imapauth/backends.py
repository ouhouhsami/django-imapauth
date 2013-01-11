from imaplib import IMAP4_SSL
from django.contrib.auth.models import User
from imapauth.settings import IMAPAUTH_HOST


class IMAPBackend(object):
    # Create an authentication method
    # This is called by the standard Django login procedure

    # ! authentificated user with this system will not be able to
    # login user admin, they are not keystaff
    def authenticate(self, username=None, password=None):
        try:
            # Check if this user is valid on the mail server
            # TODO: add settings for port, type of IMAP connection ...
            c = IMAP4_SSL(IMAPAUTH_HOST)
            c.login(username, password)
            c.logout()
        except:
            return None

        try:
            # Check if the user exists in Django's local database
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # Create a user in Django's local database
            user = User.objects.create_user(username,
                password='passworddoesntmatter')
        return user

    # Required for your backend to work properly - unchanged in most scenarios
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
