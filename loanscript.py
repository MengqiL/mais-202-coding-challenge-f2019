import pandas as pd
import matplotlib.pyplot as plt

# loading your data
df1 = pd.read_csv("loan_data.csv")
df2 = pd.read_csv("home_ownership_data.csv")

# merge the two data frames based on the member_id
df3 = df1.merge(df2, on="member_id")

# determine the average loan amount and group by home ownership
df4 = df3.groupby("home_ownership")["loan_amnt"].mean().reset_index()
print(df4)

# plot
df4.plot.bar(x="home_ownership", rot=0, width=0.6)
plt.title("Average loan amounts per home ownership")
plt.xlabel("Home ownership")
plt.ylabel("Average loan ammount ($)")

plt.show()
