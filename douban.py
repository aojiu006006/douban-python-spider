import requests
from bs4 import BeautifulSoup
import pandas as pd  # 新增
import time  # 新增

movies = []

for page in range(10):
    start = page * 25
    url = f"https://movie.douban.com/top250?start={start}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

    try:
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, "html.parser")
            items = soup.select("div.item")

            # 改成遍历所有items（去掉[:10]）
            for item in items:
                title = item.select_one("span.title").text
                rating = item.select_one("span.rating_num").text

                # 关键：把数据存进列表，而不是只print
                movies.append({"电影名": title, "评分": rating})
                print(f"已抓取：{title} {rating}")
        else:
            print(f"请求失败，状态码：{resp.status_code}")

    except Exception as e:
        print(f"第{page + 1}页出错：{e}")

    time.sleep(1)  # 关键：每次请求后休息1秒，防封IP

# 循环结束后，保存为CSV文件
df = pd.DataFrame(movies)
df.to_csv("豆瓣Top250.csv", index=False, encoding="utf-8-sig")
print(f"\n全部完成！共抓取 {len(movies)} 条数据，已保存为 豆瓣Top250.csv")
