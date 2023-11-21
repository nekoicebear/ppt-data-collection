#import contextlib 의존성 주입(필요한 기능을 선언하여 사용)

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"
#이것은 sqlite3 데베의 파일을 의미한다.

#데베와의 연결 설정.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#모든 클래스의 기본 클래스를 만든다. ORM을 사용해 데베 테이블 정의 가능.
Base = declarative_base()
#테이블과의 제약 조건의 명명 규칙을 정의
naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
Base.metadata = MetaData(naming_convention=naming_convention)

#@contextlib.contextmanager
#제너레이터
#데베 세션을 제공하는 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

"""
제너레이터: 계속 값 반환(이터레이터)를 생성해 주는 함수
이터레이터: 계속 그 다음 값을 반환.
어노테이션: 반환 값의 데이터를 미리 알려줌.
"""