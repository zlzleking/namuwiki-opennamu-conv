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
dictdata = []
rawdata_address = r"rawdata.pickle"
rawdata = open(os.path.join(rawdata_address),'rb')
dictdata = pickle.load(rawdata)
print("변환 시작합니다.")


for i in range(len(dictdata)):
    try:
        text = dictdata[i]['text']
        revision = len(dictdata[i]['contributors'])
        title = dictdata[i]['title']
        displaytitle = title
        encodedtitle = urllib.parse.quote(title)

        #print(title)

        historydir = 'history/' + encodedtitle
        datadir = 'data/'
        datapath = datadir + urllib.parse.quote(title) +'.txt'
        datafile = open( os.path.abspath(os.path.join(datapath)) ,'w')
        #print("데이터 파일 작성 완료")
        os.mkdir(os.path.abspath(os.path.join(historydir)))
        #print("히스토리 디텍토리 작성 완료")
        datafile.write(text)
        datafile.close()
        for x in range(revision):
            revisionNum = x+1
            editor = dictdata[i]['contributors'][x]
            editorfile = open(os.path.abspath(os.path.join(historydir+'/r'+str(revisionNum)+'-ip.txt')),'w')
            editorfile.write(editor)
            editorfile.close()

            datefile = open(os.path.abspath(os.path.join(historydir+'/r'+str(revisionNum)+'-today.txt')),'w')
            datefile.write(editTime)
            datefile.close()

            lengfile = open(os.path.join(historydir+'/r'+str(revisionNum)+'-leng.txt'),'w')
            lengfile.write('0')
            lengfile.close()

            revisionfile = open(os.path.join(historydir+'/r'+str(revisionNum)+'.txt'),'w')
            revisionfile.write("")
            revisionfile.close()

            sendfile = open(os.path.join(historydir+'/r'+str(revisionNum)+'-send.txt'),'w')
            sendfile.write("나무위키와 리그베다 위키에서의 편집입니다.")
            sendfile.close()
            
    except OSError as error:
        print(error)
