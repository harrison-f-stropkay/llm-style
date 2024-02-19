import pandas as pd
from tqdm import tqdm
from transformers import AutoTokenizer, OPTModel


def run(name):
    filename = f"{name}_roberta.csv"
    new_filename = f"{name}_opt.csv"

    model_name = "facebook/opt-350m"
    max_length = 2048

    model = OPTModel.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    def run_opt(s):
        inputs = tokenizer(
            s, return_tensors="pt", max_length=max_length, truncation=True
        )
        outputs = model(**inputs, output_hidden_states=True)
        last_hidden_states = outputs.hidden_states[-1]
        eos_embedding = last_hidden_states[0, -1, :]
        return eos_embedding.tolist()

    df = pd.read_csv(filename)

    column_name = "opt_eos_vector"
    df[column_name] = None

    for i in tqdm(range(len(df))):
        response = df.iloc[i]["response"]
        eos_embedding = run_opt(response)
        df.at[i, column_name] = eos_embedding

    df.to_csv(new_filename, index=False)


if __name__ == "__main__":
    names = ["authors", "temps"]
    for name in names:
        run(name)
