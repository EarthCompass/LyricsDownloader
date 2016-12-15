# -*- coding: utf-8 -*-
import os
import urllib
import urllib2
import json
import re
from tinytag import TinyTag
#def getID(song_singer)
#    url = "http://music.163.com/#/search/m/?s="+"song_singer"+"&type=1"
#   result = urllib.urlopen(url)

def	download(path,song_singer,name):
	print song_singer
	cookies = urllib2.HTTPCookieProcessor()
	opener = urllib2.build_opener(cookies)
	song_singer1 = urllib.quote(str(song_singer))
	data0 = 's='+song_singer1+'&limit=20&type=1&offset=0'
	request = urllib2.Request(
			url     = 'http://music.163.com/api/search/get/',
			headers = {'referer' : 'http://music.163.com','cookies' : 'appver=2.0.2;'},
			data    = data0)

	#nd=open('1.txt','w')
	#nd.write(opener.open(request).read())
	search_rs = json.loads(opener.open(request).read())
	url1 = 'http://music.163.com/api/song/lyric?os=pc&id='+str(search_rs['result']['songs'][0]['id'])+'&lv=-1&kv=-1&tv=-1'
	lrc = urllib2.Request(
			url     = url1 ,
			headers = {'referer' : 'http://music.163.com','cookies' : 'appver=2.0.2;'},
			)
	nd=open(path+'\\'+name+'.lrc','w')
	lrc_rs = json.loads(opener.open(lrc).read())
	try:
		nd.write(lrc_rs['lrc']['lyric'].encode('UTF-8'))
	except:
		print 'oh shit!'
	nd.close()
def scanf(dir):
	items = os.listdir(dir.decode('utf-8'))
	newlist = []
	for names in items:
		if names.endswith(".flac"):
			newlist.append(names)
	return newlist
if __name__ == '__main__':
	import sys
	reload(sys)
	sys.setdefaultencoding('utf-8')
	#download('奇迹再现')
	path = 'D:\\林俊杰\\林俊杰 - JJ陆'
	nd = open('2.txt','w+')
	for i in scanf(path):
		#download(i)
		#print i
		audiofile = TinyTag.get(path+"\\"+i)
		q = audiofile.title+" "+audiofile.artist 
		download(path,q,i[:-5])
		
		
	

