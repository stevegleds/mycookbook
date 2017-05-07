import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base # Used to create the base classes
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)  # for tutorial using in memory only
Session = sessionmaker(bind=engine) # Creates session class
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

session = Session() # Instantiate a Session to retrieve a connection  from Engine
ed_user = User(name='ed', fullname='Ed Jones', password='edspassword') # Create class instance
session.add(ed_user) # this instance is 'pending'
print('Class:', ed_user.name, ed_user.password, str(ed_user.id))
our_user = session.query(User).filter_by(name='ed').first()
print('database record:', our_user)
print(ed_user is our_user)

# Add more users with session.add_all()
session.add_all([
    User(name='Wendy', fullname='Wendy Williams', password='foobar'),
    User(name='mary', fullname='Mary Contrary', password='xxgjk'),
    User(name='fred', fullname='Fred Flinstone', password='blah')
])
ed_user.password = 'f8sdrh'
print(session.dirty) # .dirty shows any changes to existing records
print(session.new) # .new shows any new records
session.commit()
ed_user.name = 'Edwardo'
fake_user = User(name='fakeuser', fullname='Invalid', password='123')
session.add(fake_user)
print(session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all())
print(ed_user.name)
if fake_user in session:
    print('Fake user is:', fake_user.name)
else:
    print('Fake user does not exist')
session.rollback() # undo all changes since last commit()
print(ed_user.name)
if fake_user in session:
    print('Fake user is:', fake_user.name)
else:
    print('Fake user does not exist')

for instance in session.query(User).order_by(User.name):
    print(instance.name, instance.fullname)
for name, fullname in session.query(User.name, User.fullname):
    print(name, fullname)
for row in session.query(User, User.name).all():
    print(row.User, row.name)