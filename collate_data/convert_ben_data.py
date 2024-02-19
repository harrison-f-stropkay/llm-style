import json
import pandas as pd

file_paths = ["ben/temps.json", "ben/author_vectors.json", "ben/temps_vectors.json"]


def load_jsonl(file_path):
    data = []
    with open(file_path) as file:
        for line in file.readlines():
            data.append(json.loads(line))
    return data


def create_temps_data():
    with open("ben/prompts") as file:
        prompts = file.readlines()

    data = load_jsonl(file_paths[2])
    data = pd.DataFrame(data)
    data.rename(
        columns={
            "responses": "response",
            "common_vectors": "common_vector",
            "function_vectors": "function_vector",
        },
        inplace=True,
    )
    data.drop(columns=["index"], inplace=True)
    data["prompt"] = data["prompt"].apply(lambda x: prompts[int(x)].strip())
    data["response"] = data["response"].apply(lambda x: x)
    print(data.head())
    data.to_csv("ben/temps.csv", index=False, escapechar="\\")


def create_authors_data():
    data = load_jsonl(file_paths[1])
    data = pd.DataFrame(data)
    data.rename(
        columns={
            "responses": "response",
            "common_vectors": "common_vector",
            "function_vectors": "function_vector",
        },
        inplace=True,
    )
    print(data.columns)
    data.to_csv("ben/authors.csv", index=False, escapechar="\\")


if __name__ == "__main__":
    create_temps_data()
