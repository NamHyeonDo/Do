import pandas as pd
folder = "data/"
target = folder + "fkttemp.csv"
df = pd.read_csv(target)

print(df.company == "박박정")

