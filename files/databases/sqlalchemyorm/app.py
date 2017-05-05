import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base # Used to create the base classes

engine = create_engine('sqlite:///:memory:', echo=True)  # for tutorial using in memory only
# TODO find out how to create a 'real' db
'''The echo flag is a shortcut to setting up SQLAlchemy logging, which is accomplished via Python’s standard logging module. With it enabled, we’ll see all the generated SQL produced. If you are working through this tutorial and want less output generated, set it to False.'''

