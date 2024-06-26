# llm-style

Our dataset of writing prompts and responses can be found in the `hewlett` and `reddit` directories. Each contains 8 prompts with 100 responses to each prompt from human authors and each of the following LLMs:

- `gemini-1.0-pro` (generated April 25-27)
- `gemini-1.5-pro-latest` (generated April 25-27)
- `claude-3-sonnet-20240229`
- `claude-3-opus-20240229`
- `gpt-3.5-turbo-0125`
- `gpt-4-turbo-2024-04-09`

The human responses in the `hewlett` directory are from the Hewlett Foundation's [2019 Automated Scoring of Human Generated Text Responses](https://www.kaggle.com/c/asap-aes/data) dataset. The human responses in the `reddit` directory are from [Fan et al., 2018](https://github.com/facebookresearch/fairseq/blob/main/examples/stories/README.md). 

`data.ipynb` contains human response collation and LLM responses generation.

`analysis.ipynb` contains analysis of the responses using clustering, classification, and other techniques.

`results` contains classification results. 