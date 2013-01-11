===============
django-imapauth
===============

django-imapauth is a simple IMAP authentification backend for django.


Quick start
-----------

Requirements : 
* Django 1.4.3 (tested).


1. Install the app

    pypi version

    ```
    pip install django-imapauth
    ```

    development version

    ```
    pip install -e git+http://github.com/ouhouhsami/django-imapauth.git#egg=django-imapauth
    ```

2. Add ```'imapauth.backends.IMAPBackend'``` to your ```AUTHENTICATION_BACKENDS``` setting

    ```
    AUTHENTICATION_BACKENDS = (
        'imapauth.backends.IMAPBackend',
        'django.contrib.auth.backends.ModelBackend',
    )
    ```

3. Add ```IMAPAUTH_HOST``` in your settings

    ```
    IMAPAUTH_HOST = 'my_imap_host'
    ```


Usage
-----

With django-imapauth, when a user try to authenticate in your system, the ```IMAPBackend``` will try to connect to the ```IMAPAUTH_HOST``` with his credentials. 
Be careful, it's not because a user is authenticated that he can access the admin site. For that, refer to the example below, and use ```CustomIMAPBackend``` in ```AUTHENTICATION_BACKENDS```:


    from imapauth.backends import IMAPBackend

    class CustomIMAPBackend(IMAPBackend):
        def authenticate(self, username=None, password=None):
            user = super(CustomIMAPBackend, self).authenticate(username, password)
            if user is None:
                return None
            user.is_staff = True
            user.save()
            return user


Further information
-------------------

IMAPBackend copied from http://www.djangorocks.com/tutorials/creating-a-custom-authentication-backend/creating-the-imap-authentication-backend.html