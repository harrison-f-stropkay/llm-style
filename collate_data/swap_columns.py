import pandas as pd

df = pd.read_csv("authors_nltk.csv")

# swap to author,prompt,response,common_vector,function_vector
df = df[["author", "prompt", "response", "common_vector", "function_vector"]]

df.to_csv("authors_final.csv", index=False)
