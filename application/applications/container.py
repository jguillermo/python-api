# -*- coding: utf-8 -*-
from src.gamma.challenge.application.challenge_create import ChallengeCreate
from src.gamma.challenge.application.challenge_list import ChallengeList
from src.gamma.challenge.infrastructure.persistence import ChallengeRepositoryMysql


class GammaRepositoryFactory:
    @staticmethod
    def challenge_repository():
        return ChallengeRepositoryMysql()


class GammaServiceFactory:
    @staticmethod
    def challenge_list():
        return ChallengeList(repository=GammaRepositoryFactory.challenge_repository())

    @staticmethod
    def challenge_create():
        return ChallengeCreate(repository=GammaRepositoryFactory.challenge_repository())

