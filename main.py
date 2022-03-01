# ライブラリの取り込み --- (※1)
import csv
from platform import platform
from bs4 import BeautifulSoup
import urllib.request as req 
from pathlib import Path

# プラットフォームを全て取得する部分
# =========================================================================
url = "https://www.bl-n.com/services/"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")
# =======================================================================
# プラットフォーム名を全て取得する関数
contents=soup.find_all(class_="css-1kmsodk")

plat= []
for t in contents:
    plat.append(t.get("href").replace("/services/","").replace("/",""))
# print(plat)
# =================================================================================


count=len(plat)
for n in range(0,count):
    i=str(plat[n])
    # i="youtube"

    # =========================================================================
    # HTMLを解析する --- (※3)
    url = "https://www.bl-n.com/services/"+str(i)
    res = req.urlopen(url)
    soup = BeautifulSoup(res, "html.parser")
    # =======================================================================
    # タイトルを取得する関数
    contents=soup.find_all(class_="css-1gs5s70")

    title = []
    for t in contents:
        title.append(t.text)
    # print(title)

    # =======================================================================
    # プラットフォーム名を取得する関数    
    title_count=len(title)

    contents=soup.find_all(class_="css-rowkww")

    platform=str(contents[0]).replace("」で配信中のタイBLドラマ・タイドラマ一覧</h2>","").replace("<h2 class=\"css-rowkww\">「","").replace("","")

    platform_name=[]

    for n in range(0,title_count):
        platform_name.append(platform)


    # 結合=======================================================================

    data_list=list(zip(title,platform_name))
    # print(data_list)


    # # エクセルへ出力する関数
    # path=Path(r"/Users/eigo/Desktop/develop2022/drama_search/data/")


    file_title=str(i+ "のタイドラマ一覧リスト" +"2022_2_13"+ ".csv")
    with open(file_title, "w") as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerow(["作品名","プラットフォーム"])
        writer.writerows(data_list)

