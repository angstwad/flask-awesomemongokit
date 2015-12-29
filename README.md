flask-awesomemongokit
====================

An opinionated configuration for Mongo and MongoKit in Flask (singleton connections, doc registrations, indexing, and little else!)

# How does it do a thing?

In the Flask config, make a thing:

```
MONGOKIT_DOCUMENTS = [
    'package.module.DocumentClass',
    'package.module.OtherDocumentClass'
]
```

Include some config stuff, like a `MONGODB_URI` so you can connect to the DB.  Yes, URIs are the only supported config definition allowed at this time, because URIs are superior in every way (or something).  From the URI string, AwesomeMongoKit automagically determines if you need a ReplicaSet connection or not.

```
MONGO_URI = 'mongodb://localhost'
```

Optionally, include `MONGODB_KWARGS` as a list of arguments to pass into the connection class when instantiated.


Throw a Flask app instance at AwesomeMongoKit:

```
from flask import Flask
from flask.ext.awesomemongokit import AwesomeMongoKit

app = Flask(__name__)

mongo = AwesomeMongoKit(app)
```

Your document classes are automatically registered -- use the connection
attribute to access the DB connection
```
mongo.connection.DocumentClass.find({'query': 'something'})
```

Oh, and we has index helpers cuz indexing in MongoKit sucks:
```
from flask.ext.awesomemongokit import index_all_docs
from myapp import flask_app

# This ensures the index on the Document subclass
index_all_docs(flask_app)
...

```
