from transformers import BertTokenizer, BertModel
import pandas as pd
from tqdm import tqdm


def driver(name):
    filename = f"{name}_ben_pure.csv"
    new_filename = f"{name}_bert.csv"

    model_name = "bert-base-uncased"
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertModel.from_pretrained(model_name)

    def run_bert(s):
        inputs = tokenizer(s, return_tensors="pt", padding=True, truncation=True)
        outputs = model(**inputs, output_hidden_states=True)
        last_hidden_states = outputs.hidden_states[-1]
        cls_embedding = last_hidden_states[0, 0, :]
        return cls_embedding.tolist()

    df = pd.read_csv(filename)
    df["cls_vector"] = None

    for i in tqdm(range(len(df))):
        response = df.iloc[i]["response"]
        cls_embedding = run_bert(response)
        df.at[i, "cls_vector"] = cls_embedding

    df.to_csv(new_filename, index=False)


if __name__ == "__main__":
    names = ["authors", "temps"]
    for name in names:
        driver(name)
