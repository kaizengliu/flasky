# -*- coding:utf-8 -*-
# author: lkz
# date: 2015/09/25 17:01

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://lkz:asdfjkl;@10.209.68.178:3306/blog', encoding='utf-8', echo=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()
Base.query = db_session.query_property()


if __name__ == '__main__':
    from sqlalchemy import Column, Integer, String, Boolean

    class User(Base):
        __tablename__ = 'users'

        id = Column(Integer, primary_key=True)
        email = Column(String(64), unique=True, index=True)
        username = Column(String(64), unique=True, index=True)
        password_hash = Column(String(128))
        active = Column(Boolean, default=False)
        avatar_hash = Column(String(32))

    Base.metadata.create_all(engine)
    print "ok"