from applications.gamma_api.challenge import ChallengeResource
from flask_restful import Api


def add_module_gamma(api: Api):
    api.add_resource(ChallengeResource, '/challenges')
