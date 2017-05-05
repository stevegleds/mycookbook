# import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base # Used to create the base classes
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///:memory:', echo=True)  # for tutorial using in memory only
# TODO find out how to create a 'real' db
'''The echo flag is a shortcut to setting up SQLAlchemy logging, which is accomplished via Python’s standard logging module. With it enabled, we’ll see all the generated SQL produced. If you are working through this tutorial and want less output generated, set it to False.'''
Base = declarative_base()

class User(Base):
    __tablename__ = 'users' # required

    id = Column(Integer, primary_key=True) # required
    name = Column(String(50)) # lengths not required but it is good practice
    fullname = Column(String(50))
    password = Column(String(24))

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self): # optional
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

Base.metadata.create_all(engine)

ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
print(ed_user.name, ed_user.password, str(ed_user.id))