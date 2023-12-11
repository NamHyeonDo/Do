import FinanceDataReader as fdr
import matplotlib.pyplot as plt
import seaborn as
import 


tips = sns.load_dataset("tips")

sns.regplot(x="total_bill", y="tip", data=tips)
plt.show()