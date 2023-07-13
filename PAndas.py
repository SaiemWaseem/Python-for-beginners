import pandas as pd
import  numpy as np
# s = pd.Series([1,3,np.nan,7])
# print(s)
dates = pd.date_range("20230619", periods= 11)
print(dates)
df = pd.DataFrame(np.random.randn(11,4), index=dates, columns=list("SASA"))
print(df)
# dictionary
df2 = pd.DataFrame(
    {
        "A":1.0,
        "B": pd.Timestamp("20230619"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3]*4, dtype="int32"),
        "E": pd.Categorical(["test","bike","motor","car"]),
        "F": "saa"
    }
)
print(df2)
print(df2.dtypes)
c= df2[df2["C"] > 0]
print(c)
