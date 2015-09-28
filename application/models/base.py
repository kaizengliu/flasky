# -*- coding:utf-8 -*-
# author: lkz
# date: 2015/09/25 17:01

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///tmp/test.db',  encoding='utf-8')
db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.query = db_session.query_property()