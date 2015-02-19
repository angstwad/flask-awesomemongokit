#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import flask
import config
from flask.ext.raxentmongokit import RaxEntMongokit, index_helper

sys.path.insert(0, '..')

app = flask.Flask(__name__)
app.config.from_object(config)
