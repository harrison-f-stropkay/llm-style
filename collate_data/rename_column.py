import pandas as pd

df = pd.read_csv("accuracies_results.csv")
new_df = pd.DataFrame(columns=df.columns)

i = 0
for _ in range(3):
    for column_name in ["bert", "roberta", "opt", "llama", "common", "function", "cf"]:
        for _ in range(50):
            new_df.loc[i] = df.iloc[i]
            new_df.at[i, "vector"] = column_name
            i += 1

new_df.to_csv("accuracies_results_renamed.csv", index=False)
