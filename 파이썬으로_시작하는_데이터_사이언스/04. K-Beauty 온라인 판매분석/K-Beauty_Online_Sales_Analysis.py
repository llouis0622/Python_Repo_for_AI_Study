import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

%matplotlib inline

os.name
if os.name == "posix":
    sns.set(font="AppleGothic")
elif os.name == "nt":
    sns.set(font="Malgun Gothic")

pd.read_csv("data/국가_대륙_별_상품군별_온라인쇼핑_해외직접판매액_202001.csv", encoding = "cp949")
df_raw = pd.read_csv("data/국가_대륙_별_상품군별_온라인쇼핑_해외직접판매액_202001.csv", encoding = "cp949")
df_raw.shape
df_raw["국가(대륙)별"].value_counts()
df_raw[df_raw["국가(대륙)별"] == "미국"]

df_raw.melt?
df_raw.melt(id_vars=["국가(대륙)별", "상품군별", "판매유형별"])
df = df_raw.melt(id_vars=["국가(대륙)별", "상품군별", "판매유형별"], var_name="기간", value_name="백만원")
df.shape
df.head()
df.info()

df["기간"]
"2019 4/4 p)".split()
"2019 4/4 p)".split()[0]
type("2019 4/4 p)".split()[0])
int("2019 4/4 p)".split()[0])
df["기간"].map?
df["기간"].map(lambda x : int(x.split()[0]))
df["연도"] = df["기간"].map(lambda x : int(x.split()[0]))
df.head()
"2019 4/4 p)".split()[1]).split("/")
"2019 4/4 p)".split()[1]).split("/")[0]
df["분기"] = df["기간"].map(lambda x : int(x.split()[1]).split("/")[0]))
df.head()

df["백만원"].replace("-", pd.np.nan)
df["백만원"] = df["백만원"].replace("-", pd.np.nan).astype(float)
df["백만원"]
df.info()
df = df[(df["국가(대륙)별"] != "합계") & (df["상품군별"] != "합계")].copy()
df.info()
df.isnull().sum()

df_total = df[df["판매유형별"] == "계"].copy()
df_total.head()
sns.lineplot(data=df_total, x="연도", y="백만원")
sns.lineplot(data=df_total, x="연도", y="백만원", hue="상품군별")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sns.relplot(data=df_total, x="연도", y="백만원", hue="상품군별", kind="line")
sns.relplot(data=df_total, x="연도", y="백만원", hue="상품군별", kind="line", col="상품군별", col_wrap=4)
df_sub = df_total[~df_total["상품군별"].isin(["화장품"])].copy()
df_sub
sns.relplot(data=df_sub, x="연도", y="백만원", hue="상품군별", col="상품군별", col_wrap=4, kind="line")
df_sub = df_total[~df_total["상품군별"].isin(["화장품", "의류 및 패션관련 상품"])].copy()

df_total["상품군별"] == "화장품"
df_cosmetic = df_total[df_total["상품군별"] == "화장품"].copy()
df_cosmetic
df_cosmetic["상품군별"].unique()
sns.lineplot(data=df_cosmetic, x="연도", y="백만원")
plt.figure(figsize=(15, 4))
sns.lineplot(data=df_cosmetic, x="연도", y="백만원", hue="분기")

plt.figure(figsize=(15, 4))
plt.xticks(rotation=30)
sns.lineplot(data=df_cosmetic, x="기간", y="백만원")
df_cosmetic.head()
plt.figure(figsize=(15, 4))
plt.xticks(rotation=30)
sns.lineplot(data=df_cosmetic, x="기간", y="백만원", hue="국가(대륙)별")
plt.figure(figsize=(15, 4))
plt.xticks(rotation=30)
sns.lineplot(data=df_cosmetic[df_cosmetic["국가(대륙별)"] != "중국"], x="기간", y="국가(대륙)별")
plt.figure(figsize=(15, 4))
plt.xticks(rotation=30)
df_sub = df[df["판매유형별"] != "계"].copy()
sns.lineplot(data=df_sub, x="기간", y="백만원", hue="판매유형별")
plt.figure(figsize=(15, 4))
plt.xticks(rotation=30)
df_sub = df[(df["판매유형별"] != "계") & (df["판매유형별"] != "면세점")].copy()
sns.lineplot(data=df_sub, x="기간", y="백만원", hue="판매유형별", ci=None)

df_fashion = df[df["상품군별"] == "의류 및 패션관련 상품"].copy()
df_fashion.head()
df_fashion = df[(df["상품군별"] == "의류 및 패션관련 상품") & (df["판매유형별"] == "계")].copy()
df_fashion.head()
plt.figure(figsize=(15, 4))
plt.xticks(rotation=30)
sns.lineplot(data=df_fashion, x="기간", y="백만원", hue="국가(대륙)별")
df_fashion2 = df[(df["상품군별"] == "의류 및 패션관련 상품") & (df["판매유형별"] != "계")].copy()
plt.figure(figsize=(15, 4))
plt.xticks(rotation=30)
sns.lineplot(data=df_fashion2, x="기간", y="백만원", hue="판매유형별", ci=None)

df_fashion
df_fashion.pivot_table?
df_fashion.pivot_table(index="국가(대륙)별", columns="연도", values="백만원")
df_fashion.pivot_table(index="국가(대륙)별", columns="연도", values="백만원", aggfunc="sum")
df_fashion["판매유형별"].value_counts()
result = df_fashion.pivot_table(index="국가(대륙)별", columns="연도", values="백만원", aggfunc="sum")
result
sns.heatmap(result)
sns.heatmap(result, cmap = "Blues_r")
sns.heatmap(result, cmap = "Blues_r", annot=True)
plt.figure(figsize=(10, 6))
sns.heatmap(result, cmap="Blues_r", annot=True, fmt=".0f")

df_total
sns.barplot(data=df_total, x="연도", y="백만원")

plt.figure(figsize=(15, 4))
sns.lineplot(data=df_total, x="연도", y="백만원", hue="국가(대륙)별")
plt.figure(figsize=(15, 4))
sns.lineplot(data=df_total, x="연도", y="백만원", hue="상품군별")
plt.legend(bbox_to_anchor=(1.02, 1), loc=2, borderaxespad=0)