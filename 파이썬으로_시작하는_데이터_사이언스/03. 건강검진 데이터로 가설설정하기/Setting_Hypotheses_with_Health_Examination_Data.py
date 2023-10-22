import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import koreanize_matplotlib

%matplotlib inline
%config InlineBackend.figure_format = 'retina'

if os.name == 'posix':
    plt.rc("font", family="AppleGothic")
else:
    plt.rc("font", family="Malgun Gothic")

plt.rc("axes", unicode_minus=False)

pd.read_csv("data/NHIS_OPEN_GJ_2017.CSV", encoding="cp949")

df.shape
df.head()
df.tail()
df.sample()
df.info()
df.columns
df.dtypes

df.isnull()
df.isna().sum()
df.isnull().sum().plot.barh(figsize=(10, 9))
df["(혈청지오티)ALT"]
df[["(혈청지오티)ALT", "(혈청지오티)AST"]]
df["(헐청지오티)ALT"].head()
df[["(혈청지오티)ALT", "(혈청지오티)AST"]].head()
df[["(혈청지오티)ALT", "(혈청지오티)AST"]].describe()
df["성별코드"].value_counts()
df["흡연상태"].value_counts()

df.groupby(["성별코드"]).mean()
df.groupby(["성별코드"]).count()
df.groupby(["성별코드"])["가입자일련번호"].count()
df.groupby(["성별코드", "음주여부"])["가입자일련번호"].count()
df.groupby(["성별코드", "음주여부"])["감마지티피"].mean()
df.groupby(["성별코드", "음주여부"])["감마지티피"].describe()
df.groupby(["성별코드", "음주여부"])["감마지티피"].agg(["count", "mean", "median"])

df.pivot
df.pivot_table(index="성별코드", values="가입자일련번호", aggfunc="count")
df.pivot_table(index="음주여부", values="가입자일련번호", aggfunc="count")

pd.pivot_table(df, index="음주여부", values="감마지티피")
pd.pivot_table(df, index="음주여부", values="감마지티피", aggfunc=["mean", "median"])
pd.pivot_table(df, index="음주여부", values="감마지티피", aggfunc="describe")
pd.pivot_table(df, index=["음주여부", "성별코드"], values="감마지티피", aggfunc="describe")

h = df.hist(figsize=(12, 12))
h = df.iloc[:, :12].hist(figsize=(12, 12))
h = df.iloc[:, 12:24].hist(figsize=(12, 12))
h = df.iloc[:, 12:24].hist(figsize=(12, 12), bins=100)
h = df.iloc[:, 24:].hist(figsize=(12, 12), bins=100)

df.sample(1000, random_state=1)
df["음주여부"].value_counts().plot.bar()

sns.countplot(x="음주여부", data=df)
sns.countplot(x="음주여부", data=df, hue="성별코드")
sns.set(font_scale=1.5, font="AppleGothic")
sns.countplot(data=df, x="연령대코드(5세단위)", hue="음주여부")

plt.figure(figsize=(15, 4))
sns.countplot(data=df, x="신장(5Cm단위)")
plt.figure(figsize=(15, 4))
sns.countplot(data=df, x="체중(5Kg 단위)", hue="성별코드")
plt.figure(figsize=(15, 4))
sns.countplot(data=df, x="체중(5Kg 단위)", hue="음주여부")

sns.barplot(data=df, x="연령대코드(5세단위)", y="총콜레스테롤")
plt.figure(figsize=(15, 4))
sns.barplot(data=df_sample, x="연령대코드(5세단위)", y="총콜레스테롤", hue="흡연상태")
sns.barplot(data=df_sample, x="연령대코드(5세단위)", y="트리글리세라이드", hue="음주여부", ci=95)
sns.barplot(data=df_sample, x="연령대코드(5세단위)", y="트리글리세라이드", hue="음주여부", ci=sd)
sns.barplot(data=df_sample, x="연령대코드(5세단위)", y="체중(5Kg 단위)", hue="성별코드", ci=None)
sns.barplot(data=df_sample, x="연령대코드(5세단위)", y="체중(5Kg 단위)", hue="음주여부", ci=None)

plt.figure(figsize=(15, 4))
sns.lineplot(data=df, x="연령대코드(5세단위)", y="체중(5Kg 단위)", hue="성별코드")
plt.figure(figsize=(15, 4))
sns.lineplot(data=df, x="연령대코드(5세단위)", y="신장(5Cm 단위)", hue="성별코드", ci="sd")
plt.figure(figsize=(15, 4))
sns.lineplot(data=df, x="연령대코드(5세단위)", y="신장(5Cm 단위)", hue="음주여부", ci="sd")

plt.figure(figsize=(15, 4))
sns.pointplot(data=df, x="연령대코드(5세단위)", y="신장(5Cm 단위)", hue="음주여부", ci="sd")
plt.figure(figsize=(15, 4))
sns.lineplot(data=df, x="연령대코드(5세단위)", y="신장(5Cm 단위)", hue="음주여부", ci="sd")
sns.pointplot(data=df, x="연령대코드(5세단위)", y="신장(5Cm 단위)", hue="음주여부", ci="sd")
plt.figure(figsize=(15, 4))
sns.pointplot(data=df, x="연령대코드(5세단위)", y="신장(5Cm 단위)", hue="성별코드", ci="sd")
plt.figure(figsize=(15, 4))
sns.pointplot(data=df, x="연령대코드(5세단위)", y="혈색소", ci=None)
sns.pointplot(data=df, x="연령대코드(5세단위)", y="혈색소", hue="음주여부", ci=None)

plt.figure(figsize=(15, 4))
sns.boxplot(data=df, x="신장(5Cm단위)", y="체중(5Kg 단위)")
plt.figure(figsize=(15, 4))
sns.boxplot(data=df, x="신장(5Cm단위)", y="체중(5Kg 단위)", hue="성별코드")
plt.figure(figsize=(15, 4))
sns.boxplot(data=df, x="신장(5Cm단위)", y="체중(5Kg 단위)", hue="음주여부")

plt.figure(figsize=(15, 4))
sns.violinplot(data=df, x="신장(5Cm단위)", y="체중(5Kg 단위)")
plt.figure(figsize=(15, 4))
sns.violinplot(data=df_sample, x="신장(5Cm단위)", y="체중(5Kg 단위)", hue="음주여부")
plt.figure(figsize=(15, 4))
sns.violinplot(data=df_sample, x="신장(5Cm단위)", y="체중(5Kg 단위)", hue="음주여부", split=True)
plt.figure(figsize=(15, 4))
sns.violinplot(data=df_sample, x="연령대코드(5세단위)", y="혈색소", hue="음주여부", split=True)

plt.figure(figsize=(15, 4))
sns.swarmplot(data=df_sample, x="신장(5Cm단위)", y="체중(5Kg 단위)", hue="음주여부")
plt.figure(figsize=(15, 4))
sns.swarmplot(data=df_sample, x="신장(5Cm단위)", y="체중(5Kg 단위)", hue="음주여부")
sns.violinplot(data=df_sample, x="신장(5Cm단위)", y="체중(5Kg 단위)")
plt.figure(figsize=(15, 4))
sns.swarmplot(data=df_sample, x="연령대코드(5세단위)", y="혈색소", hue="음주여부")

sns.lmplot(data=df_sample, x="연령대코드(5세단위)", y="혈색소", hue="음주여부")
sns.lmplot(data=df_sample, x="연령대코드(5세단위)", y="혈색소", hue="음주여부", col="성별코드")

sns.scatterplot(data=df, x="(혈청지오티)AST", y="(혈청지오티)ALT")
sns.scatterplot(data=df_sample, x="(혈청지오티)AST", y="(혈청지오티)ALT", hue="음주여부")
sns.scatterplot(data=df_sample, x="(혈청지오티)AST", y="(혈청지오티)ALT", hue="허리둘레")
plt.figure(figsize=(8, 7))
sns.scatterplot(data=df_sample, x="(혈청지오티)AST", y="(혈청지오티)ALT", hue="음주여부", size="체중(5Kg 단위)")

sns.lmplot(data=df_sample, x="신장(5Cm단위)", y="체중(5Kg 단위)", hue="음주여부")
sns.lmplot(data=df_sample, x="신장(5Cm단위)", y="체중(5Kg 단위)", hue="성별코드", col="음주여부")
sns.lmplot(data=df_sample, x="신장(5Cm단위)", y="체중(5Kg 단위)", hue="음주여부", col="성별코드")
sns.lmplot(data=df_sample, x="신장(5Cm단위)", y="체중(5Kg 단위)", hue="흡연여부", col="음주여부")
sns.lmplot(data=df_sample, x="수축기혈압", y="이완기혈압", hue="음주여부")
sns.lmplot(data=df_sample, x="(혈청지오티)AST", y="(혈청지오티)ALT")
sns.lmplot(data=df_sample, x="(혈청지오티)AST", y="음주여부")
sns.lmplot(data=df_sample, x="(혈청지오티)AST", y="음주여부", robust=True)

df_ASLT = df_sample[(df_sample["(혈청지오티)AST"] < 400) & (df_sample["(혈청지오티)ALT"] < 400)]
df_ASLT
sns.lmplot(data=df_ASLT, x="(혈청지오티)AST", y="(혈청지오티)ALT", hue="음주여부", ci=None)
df_ASLT_high = df_sample[(df["(혈청지오티)AST"] > 400) | (df["(혈청지오티)ALT"] > 400)]
df_ASLT_high
sns.lmplot(data=df_ASLT_high, x="(혈청지오티)AST", y="(혈청지오티)ALT", hue="음주여부", ci=None)
df_ASLT_high_8000 = df_ASLT_high[df_ASLT_high["(혈청지오티)AST"] > 8000]
df_ASLT_high_8000.iloc[:, 10:27]

df_chol = df.loc[df["총콜레스테롤"].notnull(), "총콜레스테롤"]
df_chol.head()
sns.distplot(df_chol)
sns.distplot(df_chol, bins=10)

df[df["총콜레스테롤"].notnull() & (df["음주여부"] == 1)]
sns.distplot(df.loc[(df["총콜레스테롤"].notnull()) & (df["음주여부"] == 1), "총콜레스테롤"])
sns.distplot(df.loc[(df["총콜레스테롤"].notnull()) & (df["음주여부"] == 0), "총콜레스테롤"])
sns.distplot(df.loc[(df["총콜레스테롤"].notnull()) & (df["음주여부"] == 1), "총콜레스테롤"], hist=False)
sns.distplot(df.loc[(df["총콜레스테롤"].notnull()) & (df["음주여부"] == 0), "총콜레스테롤"])

sns.kdeplot(df.loc[(df["총콜레스테롤"].notnull()) & (df["음주여부"] == 1), "총콜레스테롤"])
sns.kdeplot(df.loc[(df["총콜레스테롤"].notnull()) & (df["음주여부"] == 0), "총콜레스테롤"])
sns.kdeplot(df.loc[(df["총콜레스테롤"].notnull()) & (df["음주여부"] == 1), "총콜레스테롤"], label="음주 중")
sns.kdeplot(df.loc[(df["총콜레스테롤"].notnull()) & (df["음주여부"] == 0), "총콜레스테롤"], label="음주 안 함")

plt.axvline(df_sample["총콜레스테롤"].mean(), linestyle=":")
plt.axvline(df_sample["총콜레스테롤"].median(), linestyle="--")
sns.kdeplot(df_sample.loc[(df_sample["총콜레스테롤"].notnull()) & (df["음주여부"] == 1), "총콜레스테롤"], label="음주 중")
sns.kdeplot(df_sample.loc[(df_sample["총콜레스테롤"].notnull()) & (df["음주여부"] == 0), "총콜레스테롤"], label="음주 안 함")

s_1 = df_sample.loc["음주여부"] == 1, "감마지티피"]
s_0 = df_sample.loc["음주여부"] == 0, "감마지티피"]
sns.distplot(s_1, label="음주 중")
sns.distplot(s_0, label="음주 중")

df_small = df_sample[columns]
df_corr = df_small.corr()
df_corr
df_corr["신장(5Cm단위"].sort_values()
df_corr.loc[df_corr["신장(5Cm단위"] > 0.3, "신장(5Cm단위)"]
df_corr.loc[df_corr["음주여부"] > 0.1, "음주여부"]
df_corr["음주여부"].sort_values()
df_corr.loc[df_corr["음주여부"] > 0.25, "음주여부"]
df_corr["혈색소"].sort_values(ascending=False).head(7)
df_corr["감마지티피"].sort_values(ascending=False).head(7)

plt.figure(figsize=(20, 7))
sns.heatmap(df_corr, annot=True, fmt=".2f", cmap="Blues")
mask = np.triu(np.ones_like(corr, dtype=np.bool))
plt.figure(figsize=(20, 7))
sns.heatmap(df_corr, annot=True, fmt=".2f", cmap="Blues", mask=mask)