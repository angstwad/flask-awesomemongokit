flask-raxentmongokit
====================

An opinionated configuration for Mongo and MongoKit in Flask (singleton connections and more!)

# How does it do a thing?

In the Flask config, make a thing:

```
MONGOKIT_DOCUMENTS = [
    'package.module.DocumentClass',
    'package.module.OtherDocumentClass'
]
```

Throw a Flask app instance at RaxEntMongokit:

```
from flask import Flask
from flask.ext.raxentmongokit import RaxEntMongokit

app = Flask(__name__)

mongo = RaxEntMongokit(app)
```

Your document classes are automatically registered -- use the connection 
attribute to access the DB connection
```
mongo.connection.DocumentClass.find({'query': 'something'})
```

Oh, and we has index helpers cuz no mo indexes in Mongokit:
```
from flask.ext.raxentmongokit import index_helper
from myapp.models import FooDocumentClass, BarDocumentClass

# This ensures the index on the Document subclass
index_helper(FooDocumentClass)
index_helper(BarDocumentClass)
...

```
