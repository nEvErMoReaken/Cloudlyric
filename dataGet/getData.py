# encoding=utf-8
import requests
import json
import re
import os
from bs4 import BeautifulSoup

headers = {
    'Referer': 'https://music.163.com',
    'Host': 'music.163.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
}

def get_list(artist_id):

	url = "http://music.163.com/playlist?id="+str(artist_id)

	s = requests.session()
	s = BeautifulSoup(s.get(url,headers=headers).content,"lxml")

	artist_name = s.title

	main = s.find('ul',{'class':'f-hide'})
	main = main.find_all('a')

	song = {}
	song['playlist_name'] = artist_name.text#.text方法
	song['list'] = main
	return song


def get_lyric(song_id):
    #根据歌曲id获取歌词
    list = song_id.split('=')
    id = list[1]
    url = "http://music.163.com/api/song/lyric?id=" + str(id) + "&lv=1&kv=1&tv=-1"

    s = requests.session()
    s = BeautifulSoup(s.get(url, headers=headers).content, "lxml")
    json_obj = json.loads(s.text)

    final_lyric = ""
    if ("lrc" in json_obj):
        inital_lyric = json_obj['lrc']['lyric']
        regex = re.compile(r'\[.*\]')
        final_lyric = re.sub(regex, '', inital_lyric).strip()

    return final_lyric


def makedir(dir_name):
    path = r"C:\Users\admin\PycharmProjects\Cloudlyric\data"
    dir_name = path+'./'+dir_name
    folder = os.path.exists(dir_name)
    if not folder:
        os.makedirs(dir_name)
        print("creat dir success")
    else:
        print("this folder has existed")
    return dir_name

def ConvertStrToFile(dir_name, filename, str):
    #歌词写入txt文件
    if (str == ""):
        return
    filename = filename.replace('/', '')

    text_list = ""

    for idx, line in enumerate(str.split('\n')):
        if '作曲' in line or '作词' in line or '编曲' in line:  # 去除歌词中可能出现的作词、作曲行
            continue
        if line.strip() != '':
            if ']' in line:  # []内可能是时间信息，去除
                if line.rindex(']') + 1 != len(line):
                    line = line[line.rindex(']') + 1:].strip()
                else:
                    continue
            if ':' in line:  # 冒号前面可能是歌者，应去除。e.g.: "女:"、"老狼:"
                line = line[line.rindex(':') + 1:]
            if '：' in line:  # 冒号前面可能是歌者，应去除。e.g.: "女："、"老狼："
                line = line[line.rindex('：') + 1:]
            text_list +=line.strip()
    path = r"C:\Users\admin\PycharmProjects\Cloudlyric\data"
    with open(path+"./"+dir_name + "//" + filename + ".txt", 'w',encoding='utf-8') as f:
        f.write(text_list)


def get_list_lyric(playlist_id):
    songlist = get_list(playlist_id)
    print("ok",songlist)
    playlist_name = songlist['playlist_name']
    idlist = songlist['list']

    dir=makedir(playlist_name)

    for music in idlist:
        ConvertStrToFile(playlist_name, music.text, get_lyric(music['href']))
        print("曲目： " + music.text + "  的歌词获取成功")

    print("所有文件都获取成功了")

    return dir


if __name__ == '__main__':
    dir=get_list_lyric(2618345367)