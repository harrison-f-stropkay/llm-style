import pandas as pd


def add_reddit():
    temps_df = pd.read_csv("temps.csv", escapechar="\\")
    temps_df.rename(columns={"temp": "author"}, inplace=True)
    prompts = temps_df["prompt"].unique()

    authors_df = pd.read_csv("authors.csv")
    for prompt in prompts:
        # get all responses in authors_df for this prompt with author == "reddit"
        reddit_rows = authors_df.loc[
            (authors_df["prompt"] == prompt) & (authors_df["author"] == "reddit")
        ]

        # sample 20 random reddit responses
        random_rows = reddit_rows.sample(n=20, random_state=42)

        # add these responses to temps_df
        for i in range(20):
            random_row = random_rows.iloc[i]
            new_row = {
                "prompt": prompt,
                "author": "reddit",
                "response": random_row["response"],
                "common_vector": random_row["common_vector"],
                "function_vector": random_row["function_vector"],
            }
            temps_df.loc[len(temps_df)] = new_row

    temps_df.to_csv("temps_with_reddit.csv", index=False)


if __name__ == "__main__":
    add_reddit()
