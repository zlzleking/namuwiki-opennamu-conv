# 나무위키-오픈나무 데이터 컨버터
나무위키가 배포하는 JSON파일을 오픈나무에 맞게 컨버팅하는 스크립트입니다.

오픈나무 v3.4.3-stable3 버전 기반으로 작성되었습니다. 이후 DB 변경이 있다면 작동을 보장하지 않습니다.

## 되는 것
* 나무위키의 JSON파일을 읽어서 오픈나무가 받는 형식으로 변환하기
* 문서 편집자의 종류 구별하기 (리그베다 위키,나무위키,익명)

## 의존성
1. ijson
2. sqlalchemy

## 사용법
1. set.json을 적절히 수정합니다.
2. 그 디텍토리에서 파이썬 스크립트를 실행시킵니다. 이 때 매개변수로 나무위키 json 파일을 지정해 주세요.
