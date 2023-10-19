df = pd.DataFrame(
{"a" : [4, 5, 6],
"b" : [7, 8, 9],
"c" : [10, 11, 12]},
index = [1, 2, 3])
df

df["a"]

df[["a"]]

# Rows 기준 예시
df[df.Length > 7]

# Columns 기준 예시
df[['width', 'length', 'species']]

df["a", "b"]
# 두 개 이상의 값을 불러올 때 Series형태로 불러올 경우 키값 오류가 발생합니다.

df[["a", "b"]]
# DataFrame 형태로 불러와야 합니다.

df["a"].value_counts()

df["a"].sort_values()

df.sort_values("a")

df.sort_values("a", ascending=False)

df = df.drop(["c"], axis=1)
df

df.groupby(["a"])["b"].mean()

pd.pivot_table(df, index="a")

df.plot()

df.plot.bar()

df.plot.density()