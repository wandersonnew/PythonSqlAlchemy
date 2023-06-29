from sqlalchemy import create_engine, Column, Integer, String, BigInteger, Boolean, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
engine = create_engine("mssql+pymssql://usuario:senha@host/banco", echo=False)
Session = sessionmaker(bind=engine)
session = Session()

class Base(DeclarativeBase):
    pass

# define model
class Funcionario(Base):
    __tablename__ = 'epg'
    emp_codigo = Column(String(4), primary_key=True)
    codigo = Column(String(6), primary_key=True)
    nome = Column(String(70))
# queries
funcionario = session.query(Funcionario).where(Funcionario.nome == "WANDERSON DUARTE ALVES")
for f in funcionario:
    print(f.nome)