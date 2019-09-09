#!/bin/bash

# nosetests --with-xunit -v /application/tests/unit/suite_test.py
# --cover-package=src

nosetests --cover-branches --with-coverage --cover-erase --cover-html --cover-package=/application/src --with-xunit -v /application/tests/suite_test.py
