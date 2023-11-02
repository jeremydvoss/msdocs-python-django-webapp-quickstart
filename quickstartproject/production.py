from .settings import *
import os

# Configure the domain name using the environment variable
# that Azure automatically creates for us.
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME'], 'localhost'] if 'WEBSITE_HOSTNAME' in os.environ else ["127.0.0.1"]
# ALLOWED_HOSTS = ["127.0.0.1"]

DEBUG = True
