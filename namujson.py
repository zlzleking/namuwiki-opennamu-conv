import json
import os
import pickle
import urllib.parse

revision = 0
revisionNum = 0
editor = ''
text = ""
historydir = ''
editorfilename = ''
editTime = '2016-12-07 / AM 00:00:00'
Errors = []

jsondata = "..\\namujson\\namuwiki_20160829.json"
namuwikidata = open(jsondata,'r')
print("JSON 데이터 읽기 완료")
dictdata = json.load(namuwikidata)
namuwikidata.close()
print("JSON 데이터 사전형으로 변환 완료")

print("변환 시작합니다.")


for i in range(len(dictdata)):
    try:
        text = dictdata[i]['text']
        revision = len(dictdata[i]['contributors'])
        title = dictdata[i]['title']
        displaytitle = title
        encodedtitle = urllib.parse.quote(title)



        historydir = "..\\namujson\\history\\"+ displaytitle  
        datafile = open("..\\namujson\\data\\"+ displaytitle,'w')
        #print("데이터 파일 작성 완료")
        os.mkdir(historydir)
        #print("히스토리 디텍토리 작성 완료")
        datafile.write(text)
        datafile.close()
        for x in range(revision):
            revisionNum = x+1
            editor = dictdata[i]['contributors'][x]
            editorfile = open(historydir+'\\r'+str(revisionNum)+'-ip.txt','w')
            editorfile.write(editor)
            editorfile.close()

            datefile = open(historydir+'\\r'+str(revisionNum)+'-today.txt','w')
            datefile.write(editTime)
            datefile.close()

            lengfile = open(historydir+'\\r'+str(revisionNum)+'-leng.txt','w')
            lengfile.write('0')
            lengfile.close()

            revisionfile = open(historydir+'\\r'+str(revisionNum)+'.txt','w')
            revisionfile.write("")
            revisionfile.close()

            sendfile = open(historydir+'\\r'+str(revisionNum)+'-send.txt','w')
            sendfile.write("나무위키와 리그베다 위키에서의 편집입니다.")
            sendfile.close()

            #print(displaytitle+" 문서의 "+str(revisionNum)+" 판을 저장하였고, 편집자는 "+editor+" 입니다.")
    except:
        print("Error, on "+title)
        Errors.append(title)
print("Done! "+str(len(dictdata)-len(Errors))+" Files are maden!")
