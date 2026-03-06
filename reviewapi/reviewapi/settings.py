```python
from django.core.management.utils import get_random_secret_key

SECRET_KEY = get_random_secret_key()

DEBUG = False

ALLOWED_HOSTS = ['yourdomain.com']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "yourdbname",
        "USER": "yourdbuser",
        "PASSWORD": "yourdbpassword",
        "HOST": "yourdbhost",
        "PORT": "yourdbport",
    }
}
```