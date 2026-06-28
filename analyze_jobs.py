import pandas as pd

pd.set_option("display.max_columns", None)   # 显示所有列,不省略
pd.set_option("display.width", None)         # 不限制宽度

df = pd.read_csv("jobs.csv")

# 从 location 拆出"州"(逗号后面那部分)
df["state"] = df["location"].str.split(", ").str[1]

print("=== 各州职位数(从多到少)===")
print(df["state"].value_counts())

# 筛出 title 里含 "Python" 的岗位
python_jobs = df[df["title"].str.contains("Python")]
print("=== Python 相关岗位 ===")
print(python_jobs[["title", "company", "location"]])
print("共", len(python_jobs), "个")

# 筛出 title 里含 "Engineer" 的岗位
python_jobs = df[df["title"].str.contains("Engineer")]
print("=== Engineer 相关岗位 ===")
print(python_jobs[["title", "company", "location"]])
print("共", len(python_jobs), "个")

# 给原始数据加一列:标记是否 Python 相关岗位
df["is_python"] = df["title"].str.contains("Python")

# 存一份带标记的完整数据
df.to_csv("jobs_analyzed.csv", index=False)

# 单独存一份 Python 岗位清单
python_jobs = df[df["is_python"]]
python_jobs[["title", "company", "location"]].to_csv("python_jobs.csv", index=False)

# 打印一份文字小结
print("="*40)
print("招聘数据分析报告")
print("="*40)
print(f"总岗位数:{len(df)}")
print(f"Python 相关岗位:{df['is_python'].sum()} 个")
print(f"\n各州分布:")
print(df["state"].value_counts())
print(f"\n最多的 5 个职位标题:")
print(df["title"].value_counts().head())