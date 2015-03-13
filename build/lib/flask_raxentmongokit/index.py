#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo

from raxentmongokit import RaxEntMongokit


def index_helper(mongokit_doc):
    """ Given a MongoKit document, using the "old" syntax for specifying
    collection indexes, create an index on a MongoDB collection.

    :param mongokit_doc: MongoKit Document-subclass
    :return: Results as a list of tuples in the form of
    (MongoDB parsed indexes, pymongo ensure_index result)
    """
    results = []
    for index_group in mongokit_doc.indexes:
        indexes = [(key, pymongo.ASCENDING) for key in index_group['fields']]
        mongo = RaxEntMongokit()
        db = getattr(mongo.connection, mongokit_doc.__database__)
        coll = mongokit_doc.__collection__
        unique = index_group.get('unique', False)
        result = db[coll].ensure_index(indexes, unique=unique)
        results.append((indexes, result))
    return results
