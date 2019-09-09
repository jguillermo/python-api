import unittest

from src.gamma.challenge.domain.challenge import ChallengeId
from src.gamma.challenge.infrastructure.persistence import ChallengeRepositorySql
from tests.integration import app


class ChallengeRepositorySqlTest(unittest.TestCase):
    def setUp(self):
        self.application = app

    def test_challenge_find_by_id(self):
        repository = ChallengeRepositorySql()

        challenge = repository.find_by_id(ChallengeId('7e910ed9-7e8f-4fc4-a3be-b1c5efdf5a25'))

        self.assertEqual(None, challenge)
