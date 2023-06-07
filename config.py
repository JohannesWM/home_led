import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # ...
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'k3jk24j9asu4kjkj4k5j4asdfpovq2345435jkls'
