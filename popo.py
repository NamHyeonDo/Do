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