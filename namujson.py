# 모듈 임포트
import ijson
import ipaddress
import sys
import time
from datetime import datetime
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy import Column, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Query


# 설정 로딩 및 DB 연결
with open("namu.json", "rt", encoding='UTF8') as fd:
    settings = ijson.items(fd, 'item')

Base = declarative_base()
if (settings['type'] == 'sqlite'):
    engine = create_engine(f'sqlite:///{settings["db"]}')
elif (settings['type'] == 'mysql'):
    engine = create_engine(
        f'mysql+pymysql://{settings["user"]}:{settings["pw"]}@{settings["host"]}/{settings["db"]}')
else:
    print("설정 파일이 올바르지 않습니다.")
    quit()

metadata = MetaData()
Session = sessionmaker(bind=engine)
session = Session()


# 각 테이블 정리


class table_data (Base):
    __tablename__ = 'data '
    test = Column(Text)
    title = Column(Text)
    data = Column(Text)
    type = Column(Text)


class table_history (Base):
    __tablename__ = 'history '
    id = Column(Text)
    title = Column(Text)
    data = Column(Text)
    date: Column(Text)
    ip: Column(Text)
    send: Column(Text)
    leng: Column(Text)
    hide: Column(Text)
    type: Column(Text)


# IP인지 여부 판단
def checkip(addr):
    try:
        ip = ipaddress.ip_address(addr)
        return True
    except ValueError:
        return False

# 편집자를 구분하는 부분입니다. 리그베다 위키 유저는 R:로, 나무위키 유저는 N:의 Prefix가 붙습니다.


def editorProcess(editor):
    if editor.find("R:") != -1:
        pass
    elif checkip(editor) == True:
        pass
    else:
        editor = "N:"+editor
    return editor


def mainprocess():
    doc_count = 0

    # 이하의 코드는 문서별로 실행됩니다.
    try:
        with open(sys.argv[0], "rt", encoding='UTF8') as fd_json:
            docs = ijson.items(fd_json, 'item')
            for item in docs:
                title = item['title']
                text = item['text']
                author = item['contributers']
                data_buf = table_data(None, title, text, None)
                session.add(data_buf)
                revision = 0
                for editor in author:
                    timestamp = time.mktime(datetime.strptime(
                        datetime.datetime.now(), '%Y-%m-%d %H:%M:%S').timetuple())
                    history_buf = table_history(str(revision), title, text, str(
                        timestamp), editorProcess(editor), None, str(0), None, None)
                    session.add(history_buf)
                session.commit()
                doc_count = doc_count + 1
                print(f"문서 {title} 변환 완료.")

    except Exception as e:
        print("에러 발생 : ", e)
        print("맞는 나무위키 덤프 json을 입력했는지 확인해 주세요.")
    print("문서 변환 작업이 종료되었습니다.")
    print(str(doc_count)+"개의 문서가 변환되었습니다.")


print("이 스크립트는 나무위키 JSON 데이터가 필요합니다. 데이터를 로딩합니다.\n")
mainprocess()
