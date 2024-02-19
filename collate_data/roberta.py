from transformers import RobertaTokenizer, RobertaModel
import pandas as pd
from tqdm import tqdm


def driver(name):
    filename = f"{name}_bert.csv"
    new_filename = f"{name}_roberta.csv"

    model_name = "roberta-base"  # Use the RoBERTa model
    tokenizer = RobertaTokenizer.from_pretrained(model_name)
    model = RobertaModel.from_pretrained(model_name)

    def run_roberta(s):
        inputs = tokenizer(s, return_tensors="pt", padding=True, truncation=True)
        outputs = model(**inputs, output_hidden_states=True)
        last_hidden_states = outputs.hidden_states[-1]
        cls_embedding = last_hidden_states[0, 0, :]
        return cls_embedding.tolist()

    df = pd.read_csv(filename)
    df["roberta_cls_vector"] = None

    for i in tqdm(range(len(df))):
        response = df.iloc[i]["response"]
        cls_embedding = run_roberta(response)
        df.at[i, "roberta_cls_vector"] = cls_embedding

    df.to_csv(new_filename, index=False)


if __name__ == "__main__":
    names = ["authors", "temps"]
    for name in names:
        driver(name)
