# -*- coding: utf-8 -*-
import os
import urllib
import urllib2
import json
from tinytag import TinyTag

def scan1(dir):
	filelist = []
	for root,dirs,files in os.walk(dir):
		#print files,root,dirs
		for file in files:
			if os.path.join(root,file).endswith(".flac"):
				filelist.append(os.path.join(root,file))
	return filelist
def	download1(path,song_singer):
	print song_singer
	cookies = urllib2.HTTPCookieProcessor()
	opener = urllib2.build_opener(cookies)
	song_singer1_url = urllib.quote(str(song_singer))
	data0 = 's='+song_singer1_url+'&limit=20&type=1&offset=0'
	request = urllib2.Request(
			url     = 'http://music.163.com/api/search/get/',
			headers = {'referer' : 'http://music.163.com','cookies' : 'appver=2.0.2;'},
			data    = data0)
	search_rs = json.loads(opener.open(request).read())
	try:
		url1 = 'http://music.163.com/api/song/lyric?os=pc&id='+str(search_rs['result']['songs'][0]['id'])+'&lv=-1&kv=-1&tv=-1'
		lrc = urllib2.Request(
				url     = url1 ,
				headers = {'referer' : 'http://music.163.com','cookies' : 'appver=2.0.2;'},
				)
		lrc_rs = json.loads(opener.open(lrc).read())
		try:
			nd=open(path[:-5]+'.lrc','w')
			nd.write(lrc_rs['lrc']['lyric'].encode('UTF-8'))
			nd.close()
			print 'Success! '+song_singer
		except:
			print 'Failed! '+str(song_singer)+' no lyric'
	except:
		print 'Failed! '+str(song_singer)+' not found'
if __name__ == '__main__':
	import sys
	reload(sys)
	sys.setdefaultencoding('utf-8')
	path = "H:\\MUSIC\\林俊杰\\"  #歌曲路径
	for i in scan1(path):
		try:
			audiofile = TinyTag.get(i)
			q = audiofile.title+" "+audiofile.artist
			#download(path,q,i[:-5])
			download1(i,q)
		except:
			print 'Failed!'+' some wrong with file name '
