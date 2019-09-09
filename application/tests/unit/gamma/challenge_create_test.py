import unittest
from unittest import mock

from src.gamma.challenge.application.challenge_create import ChallengeCreate, ChallengeCreateInput
from src.gamma.challenge.domain.challenge import ChallengeRepository, Challenge, ChallengeId, ChallengeTitle
from src.shared.domain.types import TypeUuid
from src.shared.exception import BadRequest

CHALLENGE_ID = 'ee5de924-11e4-459f-ae37-8ff32860db60'


class ChallengeMockRepository:

    @staticmethod
    def ok() -> ChallengeRepository:
        challenge = Challenge(ChallengeId(CHALLENGE_ID), ChallengeTitle('a'))
        repository = mock.create_autospec(ChallengeRepository)
        repository.find_all.return_value = [
            challenge,
            Challenge(ChallengeId('b4d51f9e-cc29-4e52-a351-4156149b3ef1'), ChallengeTitle('b'))
        ]

        repository.find_by_id.return_value = challenge

        repository.persist.return_value = True

        return repository

    @staticmethod
    def find_by_id_empty() -> ChallengeRepository:
        repository = mock.create_autospec(ChallengeRepository)
        repository.find_by_id.return_value = None
        repository.persist.return_value = True
        return repository


class TestGammaApplicationChallengeCreate(unittest.TestCase):

    def test_exception_input_validate(self):
        with self.assertRaises(BadRequest):
            ChallengeCreateInput('sdf', 'titulo')

    def test_exception_ya_existe_el_id(self):
        with self.assertRaises(BadRequest):
            service = ChallengeCreate(ChallengeMockRepository.ok())
            input = ChallengeCreateInput(CHALLENGE_ID, 'titulo')
            service.excecute(input)

    def test_create_ok(self):
        service = ChallengeCreate(ChallengeMockRepository.find_by_id_empty())
        input = ChallengeCreateInput(CHALLENGE_ID, 'titulo')

        self.assertEqual(True, service.excecute(input))
