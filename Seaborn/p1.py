import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df= sns.load_dataset('d')

sns.scatterplot(df, x='elo_i', y='team_id')
plt.show()