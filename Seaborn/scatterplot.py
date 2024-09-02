import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# x1=[20,34, 49, 43, 22]
# y1=[70,60, 89, 53, 44]

# sns.barplot(x=x1, y=y1)
# plt.show()

df= pd.read_csv('d.csv')
sns.scatterplot(data=df, x='year_id', y='date_game')
plt.show()