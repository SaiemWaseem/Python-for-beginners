import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
# from numpy import median
film = sns.load_dataset("titanic")
print(film)
sns.barplot(x='who',y='alone', hue='sex',data=film, color='red',estimator= median, palette='pastel')
plt.show()
import matplotlib.pyplot as plt
import seaborn as sns
# import numpy as np
import pandas as pd

kashti = sns.load_dataset('titanic')
x=kashti.head()
print(x)
x = sns.boxplot(x= "survived",
            y= "age", showmeans=True,
            meanprops= {"marker":"+",
                        "markersize":"12",
                        "markeredgecolor":"red"},
            data=kashti)
plt.xlabel("How many survived")
plt.ylabel("Age(year)")
plt.title("Box Plot")

plt.show()
print(x)
