from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return f'<User(name={self.name}, fullname={self.fullname}, nickname={self.nickname})>'

if __name__ == '__main__':
    Base.metadata.create_all(engine)

    # rhe_user = User(name='Rheanne', fullname='Rheanne McIntosh', nickname='Rhe')
    # print(rhe_user.name)
    # print(rhe_user.id)

    # session.add(rhe_user)
    # session.commit()
    # print(rhe_user.id)

    new_users = [
        User(name='Grace', fullname='Grace Hopper', nickname='Pioneer'),
        User(name='Alan', fullname='Alan Turing', nickname='Computer Scientist'),
        User(name='Katherine', fullname='Katherine Johnson', nickname='')
    ]

    session.add_all(new_users)
    session.commit()

    for user in new_users:
        print(user.id)
