import pandas as pd
import torch
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModel


def run(name):
    filename = f"{name}_opt.csv"
    new_filename = f"{name}_llama.csv"

    model_name = "meta-llama/Llama-2-7b-hf"
    model = AutoModel.from_pretrained(model_name, device_map="auto", load_in_8bit=True)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    max_length = 1024

    def run_llama(s):
        inputs = tokenizer(
            s, return_tensors="pt", max_length=max_length, truncation=True
        )
        outputs = model(**inputs, output_hidden_states=True)
        last_hidden_states = outputs.hidden_states[-1]
        vector = last_hidden_states[0, -1, :]
        return vector.tolist()

    df = pd.read_csv(filename)

    column_name = "llama"
    df[column_name] = None

    for i in tqdm(range(len(df))):
        response = df.iloc[i]["response"]
        vector = run_llama(response)
        df.at[i, column_name] = vector

    df.to_csv(new_filename, index=False)


if __name__ == "__main__":
    names = ["authors", "temps"]
    names = ["temps"]
    for name in names:
        run(name)
