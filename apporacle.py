from sqlalchemy import create_engine, Column, Integer, String, BigInteger, Boolean, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase

engine = create_engine("oracle+cx_oracle://usuario:senha@host:porta/orcl")
Session = sessionmaker(bind=engine)
session = Session()

class Base(DeclarativeBase):
    pass

# define model
class Paciente(Base):
    __tablename__ = 'paciente'
    cd_paciente = Column(Integer, primary_key=True)
    nm_paciente = Column(String(200))
# queries
funcionario = session.query(Paciente).where(Paciente.cd_paciente == 38025)
for f in funcionario:
    print(f.nm_paciente)