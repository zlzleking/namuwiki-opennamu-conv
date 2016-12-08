# 모듈 임포트
import json
import os
import pickle
import urllib.parse

# 숫자 판단
def isNumber(data):
  try:
    tmp1 = float(data)
    return True
  except ValueError:
    return False

# 편집자를 구분하는 부분입니다. 리그베다 위키 유저는 R:로, 나무위키 유저는 N:의 Prefix가 붙습니다.
def editorProcess(editor):
	if editor.find("R:") != -1:
		pass
	elif isNumber(editor[0]) == True:
		pass
	else:
		editor = "N:"+editor
	print(editor)
	return editor
	



def mainprocess(dictdata):

	revision = 0
	revisionNum = 0
	editTime = '나무위키 덤프로부터 생성된 파일'
	Errorlist = []

	# 이하의 코드는 문서별로 실행됩니다.
	for i in range(5):
		try:
			# 데이터를 읽어서 본문, 문서 제목, 리비전 수를 셉니다. 또한 문서 제목을 사전에 인코딩합니다.
			text = dictdata[i]['text']
			revision = len(dictdata[i]['contributors'])
			title = dictdata[i]['title']
			displaytitle = title
			encodedtitle = urllib.parse.quote(title).replace('/','%2F')
		
			# 데이터 디텍토리를 지정하고, 데이터가 들어갈 경로를 구합니다.
			datadir = 'data/'
			datapath = datadir + encodedtitle +'.txt'

			# 데이터를 기록합니다.
			datafile = open( os.path.abspath(os.path.join(datapath)) ,'w')
			datafile.write(text)
			datafile.close()
		
			# 편집 이력이 들어갈 디텍토리를 만들고, 그 경로를 지정합니다.
			historydir = 'history/' + encodedtitle
			os.mkdir(os.path.abspath(os.path.join(historydir)))
			
        
			# 이하의 코드는 리비전별로 실행됩니다.
			for x in range(revision):
			
				revisionNum = x+1
			
				# 편집자 기록을 만듭니다.
				editor = dictdata[i]['contributors'][x]
				editor = editorProcess(editor)
				print(editor)
				editorfile = open(os.path.abspath(os.path.join(historydir+'/r'+str(revisionNum)+'-ip.txt')),'w')
				editorfile.write(editor)
				editorfile.close()

				# 편집 시간 기록을 만듭니다.
				datefile = open(os.path.abspath(os.path.join(historydir+'/r'+str(revisionNum)+'-today.txt')),'w')
				datefile.write(editTime)
				datefile.close()

				# 가짜 리비전들을 생성합니다. 생성값은 모두 공백이 됩니다.
				revisionfile = open(os.path.join(historydir+'/r'+str(revisionNum)+'.txt'),'w')
				revisionfile.write("")
				revisionfile.close()

				# 편집 코멘트를 생성합니다.
				sendfile = open(os.path.join(historydir+'/r'+str(revisionNum)+'-send.txt'),'w')
				sendfile.write("나무위키와 리그베다 위키에서의 편집입니다.")
				sendfile.close()
            
		except OSError as error:
			print(error)
			Errorlist.append(title)
		
	print("문서 변환 작업이 종료되었습니다.")
	print(str(len(dictdata))+"개의 문서가 데이터에 존재합니다. 그 중 "+str((len(dictdata)-len(Errorlist)))+"개의 문서가 변환되었습니다. 오류가 발생한 문서는 "+str(len(Errorlist))+" 개 입니다.")


print("스크립트의 실행 환경을 확인합니다")
if os.path.exists(os.path.join("./history")) == False:
	os.mkdir(os.path.join("./history"))
if os.path.exists(os.path.join("./data")) == False:
	os.mkdir(os.path.join("./data"))
print("실행 환경 확인이 종료되었습니다.")

print("이 스크립트는 나무위키 JSON 데이터가 필요합니다. 데이터를 로딩합니다.\n 만약 이 스크립트를 이전에 실행한 적이 있으시다면, 그때 생성된 임시 파일을 사용합니다.")

if os.path.exists(os.path.join("rawdata.pickle")) == True:
	print("임시 파일이 로딩되었습니다.")
	rawdata_address = r"rawdata.pickle"
	rawdata = open(os.path.join(rawdata_address),'rb')
	dictdata = pickle.load(rawdata)
	

else :
	print("임시 파일이 없으므로 JSON을 로딩합니다.")
	jsondata = os.path.join(namuwikidata.json)
	namuwikidata = open(jsondata,'r')
	print("JSON 데이터 읽기 완료")
	dictdata = json.load(namuwikidata)
	namuwikidata.close()
	print("JSON 데이터 사전형으로 변환 완료")
	
print("모든 사전 작업이 종료되었습니다. 변환을 시작합니다.")
mainprocess(dictdata)