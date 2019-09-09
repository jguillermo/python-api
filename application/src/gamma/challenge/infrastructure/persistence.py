from applications.db import db
from src.gamma.challenge.domain.challenge import ChallengeRepository, Challenge, ChallengeId, ChallengeTitle


class ChallengeModel(db.Model):
    __tablename__ = 'challenge'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))

    def __init__(self, name, title):
        self.name = name
        self.title = title

    def persist(self) -> None:
        db.session.add(self)
        db.session.commit()


class ChallengeRepositorySql(ChallengeRepository):

    def find_all(self):
        challenge_models = ChallengeModel.query.filter_by()
        data = []
        for item in challenge_models:
            data.append(self._model_to_entity(item))
        return data

    def find_by_id(self, id: ChallengeId):
        challenge_model = ChallengeModel.query.filter_by(id=id.value()).first()
        return self._model_to_entity(challenge_model)

    def _model_to_entity(self, model: ChallengeModel) -> Challenge:
        if model is None:
            return None

        return Challenge.create(ChallengeId(model.id), ChallengeTitle(model.title))

    def persist(self, challenge: Challenge):
        challenge_model = ChallengeModel(challenge.id.value(), challenge.title.value())
        challenge_model.persist()
        return True
