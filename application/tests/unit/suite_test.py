# -*- coding: utf-8 -*-

import unittest

from tests.unit.gamma.challenge_create_test import TestGammaApplicationChallengeCreate
from tests.unit.gamma.challenge_list_test import TestGammaApplicationChallengeList
from tests.unit.shared.exception_test import TestSharedDomainException
from tests.unit.shared.validator import TestSharedDomainValidatorIsNone, TestSharedDomainValidatorString, \
    TestSharedDomainValidatorInteger, TestSharedDomainValidatorIntegerPositive, TestSharedDomainValidatorDate


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromModule(TestSharedDomainValidatorIsNone))
    suite.addTests(loader.loadTestsFromModule(TestSharedDomainValidatorString))
    suite.addTests(loader.loadTestsFromModule(TestSharedDomainValidatorInteger))
    suite.addTests(loader.loadTestsFromModule(TestSharedDomainValidatorIntegerPositive))
    suite.addTests(loader.loadTestsFromModule(TestSharedDomainValidatorDate))
    suite.addTests(loader.loadTestsFromModule(TestSharedDomainException))

    suite.addTests(loader.loadTestsFromModule(TestGammaApplicationChallengeList))
    suite.addTests(loader.loadTestsFromModule(TestGammaApplicationChallengeCreate))
    return suite


if __name__ == '_main_':
    unittest.TextTestRunner(verbosity=2).run(suite())
