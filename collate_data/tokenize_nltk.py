import pandas as pd
from nltk.tokenize import word_tokenize


df = pd.read_csv("authors.csv")

df["response"] = df["response"].apply(lambda x: " ".join(word_tokenize(x)).strip())

df.to_csv("authors_nltk.csv", index=False)
