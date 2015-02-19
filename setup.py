from setuptools import setup

setup(
    name='flask-raxentmongokit',
    version='0.1',
    packages=['flask_raxentmongokit'],
    url='https://github.rackspace.com/EnterpriseSupport/raxent-mongokit',
    license='None',
    author='Rackspace Enterprise DevOps',
    author_email='',
    description='Helpers to make MongoKit "opinionated" in our environments',
    requires=[
        'mongokit',
        'pymongo',
        'flask'
    ]
)
