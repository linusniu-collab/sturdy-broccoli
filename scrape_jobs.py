import requests
from bs4 import BeautifulSoup
import pandas as pd

# ---------- 第一步:抓网页 ----------
url = "https://realpython.github.io/fake-jobs/"
resp = requests.get(url)                        # 把整个网页抓下来
soup = BeautifulSoup(resp.text, "html.parser")  # 解析成能查找的结构

# ---------- 第二步:解析出每条职位 ----------
cards = soup.find_all("div", class_="card-content")  # 找到全部职位卡片(100个)

jobs = []                                  # 准备一个列表装结果
for card in cards:                         # 遍历每个卡片
    job = {
        "title":   card.find("h2", class_="title").text.strip(),
        "company": card.find("h3", class_="company").text.strip(),
        "location":card.find("p", class_="location").text.strip(),
        "date":    card.find("time").text.strip(),
    }
    jobs.append(job)                       # 每条存成一个字典,塞进列表

# ---------- 第三步:存成 csv ----------
df = pd.DataFrame(jobs)                     # 列表套字典 → DataFrame(还记得吗!)
df.to_csv("jobs.csv", index=False)
print(f"爬完了,共 {len(df)} 条,已存到 jobs.csv")
print(df.head())