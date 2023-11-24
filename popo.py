import FinanceDataReader as fdr
ksp = fdr.DataReader("KS11", "2001")
print(ksp)
print("\n----------------------------------------------\n")

""" res = ksp["High"].max()
print(res)

res = ksp["High"].idxmax()
print(res)

res = ksp["Low"].min()
print(res) """

""" res = ksp["Volume"].nlargest(n=5)
print(res)

res = ksp["Close"].nsmallest(n=5)
print(res)

cond = ksp["Close"] >= 3000
res = ksp[cond].index[0]
print(res)

res = ksp["Volume"] > ksp["Volume"].shift()
print(res)

res = ksp["up"] != ksp["up"].shift().cumsum()
print(res)

res = ksp["grp"].groupby(ksp["grp"].values).cumcount() + 1
print(res)

res = ksp["up_cnt"].max()
print(res) """

""" d.read_csv(target, encoding="CP949")
df.to_csv("./data/apttt.csv", encoding="utf8")

df.rename(columns={"분양가격(제곱미터)":"분양가"})

df.dtypes
df["분양가"].convert_dtypes()
df.dtypes

df.to_numpy() """