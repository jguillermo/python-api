from sqlalchemy import Table, Column, String, CHAR, Boolean, Text, SmallInteger, Integer, DateTime, ForeignKey, DECIMAL
from sqlalchemy.orm import mapper, relationship

from src.gamma.auth.domain.student import StudentAccess
from src.gamma.challenge.domain.challenge import Challenge
from src.gamma.progress.domain.point import Level
from src.gamma.progress.domain.progress import Student, ProgressItem, Progress
from src.gamma.reward.domain.claim import Claim
from src.gamma.reward.domain.reward import Reward


def load_mapper_gm(metadata_app):
    challenge = Table('gm_challenge', metadata_app,
                      Column('id', CHAR(36), primary_key=True),
                      Column('project', String(50), nullable=True),
                      Column('title', String(200), nullable=True),
                      Column('description', Text, nullable=True),
                      Column('score', Integer, nullable=True),
                      Column('start_at', DateTime, nullable=True),
                      Column('duration', Integer, nullable=True),
                      Column('status', String(50), nullable=True),
                      Column('challenge_number', Integer, nullable=True),
                      Column('challenge_event', String(50), nullable=True),
                      Column('order', Integer, nullable=True),
                      Column('stock', Integer, nullable=True),
                      Column('level', Integer, nullable=True),
                      Column('created_at', DateTime, nullable=True),
                      )
    mapper(Challenge, challenge)

    student = Table('gm_student', metadata_app,
                    Column('id', CHAR(36), primary_key=True),
                    Column('name', String(100), nullable=True),
                    Column('last_name', String(100), nullable=True),
                    Column('code', String(15), nullable=True),
                    Column('campus', String(100), nullable=True),
                    Column('created_at', DateTime, nullable=True)
                    )

    mapper(Student, student)

    progress_item = Table('gm_progress_item', metadata_app,
                          Column('id', CHAR(36), primary_key=True),
                          Column('challenge_event', String(50), nullable=True),
                          Column('student_id', CHAR(36), ForeignKey('gm_student.id'), nullable=False),
                          Column('created_at', DateTime, nullable=True)
                          )
    mapper(ProgressItem, progress_item, properties={
        'student': relationship(Student)
    })

    progress = Table('gm_progress', metadata_app,
                     Column('id', CHAR(36), primary_key=True),
                     Column('total', Integer, nullable=True),
                     Column('progress', Integer, nullable=True),
                     Column('status', String(50), nullable=True),
                     Column('challenge_id', CHAR(36), nullable=True),
                     Column('student_id', CHAR(36), ForeignKey('gm_student.id'), nullable=False),
                     Column('date_start', DateTime, nullable=True),
                     Column('date_end', DateTime, nullable=True),
                     Column('seen', Boolean, nullable=True),
                     Column('created_at', DateTime, nullable=True),
                     Column('complete_at', DateTime, nullable=True),

                     )
    mapper(Progress, progress, properties={
        'student': relationship(Student)
    })

    level = Table('gm_level', metadata_app,
                  Column('id', CHAR(36), primary_key=True),
                  Column('level', Integer, nullable=True),
                  Column('min_point', Integer, nullable=True),
                  Column('max_point', Integer, nullable=True),
                  Column('created_at', DateTime, nullable=True)
                  )
    mapper(Level, level)

    reward = Table('gm_reward', metadata_app,
                   Column('id', CHAR(36), primary_key=True),
                   Column('point', Integer, nullable=True),
                   Column('stock', Integer, nullable=True),
                   Column('expiration', DateTime, nullable=True),
                   Column('title', String(100), nullable=True),
                   Column('image', String(150), nullable=True),
                   Column('description', Text, nullable=True),
                   Column('requirement', Text, nullable=True),
                   Column('condition', Text, nullable=True),
                   Column('map', String(100), nullable=True),
                   Column('created_at', DateTime, nullable=True)
                   )
    mapper(Reward, reward)

    claim = Table('gm_claim', metadata_app,
                  Column('id', CHAR(36), primary_key=True),
                  Column('code', String(100), nullable=True),
                  Column('status', String(20), nullable=True),
                  Column('student_id', CHAR(36), primary_key=True),
                  Column('reward_id', CHAR(36), primary_key=True),
                  Column('score', Integer, nullable=True),
                  Column('claimed_at', DateTime, nullable=True),
                  Column('created_at', DateTime, nullable=True)
                  )
    mapper(Claim, claim)

    student_access = Table('gm_student_access', metadata_app,
                           Column('code', CHAR(9), primary_key=True)
                           )
    mapper(StudentAccess, student_access)
