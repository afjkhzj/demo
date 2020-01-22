import requests
import json

def get_song(SongName):
    url = "http://www.xiaoxina.cn/api.php?s=" + SongName + "&num=10"
    req=requests.get(url)
    html=json.loads(req.text)
    for item in html:
        print(item["name"],item["picLink"],item["id"],item["singer"],item["url"])


if __name__ == "__main__":
    SongName=input("请输入歌名:")
    get_song(SongName)