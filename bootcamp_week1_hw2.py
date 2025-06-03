#1
import seaborn as sns
import pandas as pd

df = sns.load_dataset("car_crashes")


new_cols = ["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]

print(new_cols)

#2


df = sns.load_dataset("car_crashes")

new_cols = [col.upper() + "_FLAG" if "NO" not in col.upper() else col.upper() for col in df.columns]

print(new_cols)

#3

df = sns.load_dataset("car_crashes")
og_list = ["abbrev", "no_previous"]

new_df = df[[col for col in df.columns if col not in og_list]]

print(new_df.head())
