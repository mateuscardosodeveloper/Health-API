from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from models import Base


class Users(Base):
    __tablename__ = 'USERS'

    uuid = Column(String, primary_key=True)
    username = Column(String, unique=True) # TODO: This field need be unique not workin
    password = Column(String)

    def __repr__(self):
        return f"User({self.username})"


class Patients(Base):
    __tablename__ = 'PATIENTS'

    uuid = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(DateTime)

    def __repr__(self):
        return f"Patient({self.first_name} {self.last_name})"


class Pharmacies(Base):
    __tablename__ = 'PHARMACIES'

    uuid = Column(String, primary_key=True)
    name = Column(String)
    city = Column(String)

    def __repr__(self):
        return f"Pharmacie({self.name})"


class Transactions(Base):
    __tablename__ = 'TRANSACTIONS'

    uuid = Column(String, primary_key=True)
    patient_uuid = Column(String, ForeignKey('PATIENTS.uuid'))
    pharmacy_uuid = Column(String, ForeignKey('PHARMACIES.uuid'))
    amount = Column(Integer)
    timestamp = Column(DateTime)

    patient = relationship('Patients', backref='TRANSACTIONS')
    pharmacy = relationship('Pharmacies', backref='TRANSACTIONS')

    def __repr__(self):
        return f'Transaction({self.uuid})'
