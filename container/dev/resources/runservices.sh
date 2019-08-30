#!/bin/bash

gunicorn -c /resources/gunicorn.py wsgi:app
