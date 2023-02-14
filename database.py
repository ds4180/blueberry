from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from starlette.config import Config

config = Config('.env')
DATABASE = config('DATABASE')

# import contextlib 

##
#######################
import pymysql

pymysql.install_as_MySQLdb()
#######################
##


# user_name = "root"
# user_pwd = "4180"
# db_host = "127.0.0.1"
# db_name = "test"

# DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
#     user_name,
#     user_pwd,
#     db_host,
#     db_name,
# )

ENGINE = create_engine(
    DATABASE,
    # connect_args={"check_same_thred":False} ##sqlite인경우만 필요함.
    
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)

Base = declarative_base()

# @contextlib.contextmanager
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
