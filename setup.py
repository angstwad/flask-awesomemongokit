from setuptools import setup

import flask_raxentmongokit

setup(
    name='flask-raxentmongokit',
    version=flask_raxentmongokit.__version__,
    packages=['flask_raxentmongokit'],
    url='https://github.rackspace.com/EnterpriseSupport/raxent-mongokit',
    license='None',
    author='Rackspace Enterprise DevOps',
    author_email='',
    description='Helpers to make MongoKit "opinionated" in our environments',
    install_requires=[
        'mongokit',
        'pymongo',
        'flask'
    ]
)
