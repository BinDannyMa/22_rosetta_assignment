import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("score_rms.dat")

sns.relplot(x="rms", y="score", data=df)
plt.savefig("scoreVSrms.png")



