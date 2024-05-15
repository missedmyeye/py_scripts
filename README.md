# py_scripts
Python scripts for multiple purposes. Currently in progress: Text Generation with LLM, Word Frequency in Documents.
## Pre-requisites
- [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/)
## Text Generation with LLM
### Overview
The purpose of this script is to generate text from a chosen LLM via HuggingFace Inference API with an input text.
### Creating an environment
Proceed to create Python environment using miniconda. Adjust `requirements.txt` as per your needs if necessary, then install the required packages specified. Currently only `python-dotenv` is used.
```
conda env create -n env_name python=3.10
conda activate env_name
pip install -r requirements.txt
```
### Get your API Token
For this script, we are using Hugging Face Inference API, you will be required to use an API Token, [instructions to obtain provided here](https://huggingface.co/docs/api-inference/quicktour#get-your-api-token).<br>
Following which, please create a `.env` file in the repository root folder. Its contents should contain your token like so:
```
API_TOKEN = hf_xxxxxxxx
```
### Quickstart
If not done, use your terminal to navigate to the root folder of the repository.<br>
Run `gen_run.sh` to run the script, if no input is submitted, it will run with the default input provided in `gen_config.json`
```bash
$ ./gen_run.sh
Enter input: Money is the root of

Input: Money is the root of
Generated Text: Money is the root of evil that we see across the world. It is the root of our failures because we lack the self-respect, trust and good governance we need to overcome all these problems and to become powerful enough to stop suffering and take responsibility
```
Should you encounter permission issues, grant permission to run the script.
```bash
chmod +x gen_run.sh
```
### Alternative Methods of Running
If running the python script `textgen.py` directly, assuming you have navigated to the root folder:
```bash
$ python src/textgen.py "Money is the root of"

Input: Money is the root of
Generated Text: Money is the root of evil that we see across the world. It is the root of our failures because we lack the self-respect, trust and good governance we need to overcome all these problems and to become powerful enough to stop suffering and take responsibility
```
### Parameter Adjustment
Apart from the default text input, other parameters are available to adjust in the config file `gen_config.json`. Details can be found [here](https://huggingface.co/docs/api-inference/detailed_parameters#text-generation-task) as well. For this script, adjustable parameters will be limited to this list provided.
- `API_URL`: For determining which model is used for inference
- `input`: Default text input to the model
- `max_new_tokens`: Int (0-250). The amount of new tokens to be generated, this does not include the input length it is a estimate of the size of generated text you want. Each new tokens slows down the request, so look for balance between response times and length of text generated.
- `num_return_sequences`: Integer. The number of proposition you want to be returned.
- `temperature`: Float (0.0-100.0). The temperature of the sampling operation. 1 means regular sampling, 0 means always take the highest score, 100.0 is getting closer to uniform probability.<br>
Here is an example of the format of `gen_config.json`:
```
[
    {
        "API_URL":"https://api-inference.huggingface.co/models/gpt2",
        "input": "Life is a box of",
        "max_new_tokens":50,
        "num_return_sequences":1,
        "temperature":0.8
    }
]
```
## Word Frequency with Ranking in Documents
### Overview
The purpose of this script is to print the top (start rank)th to (end rank)th words
in a provided document by frequency, without the usage of third-party libraries.
### Creating an environment
Proceed to create Python environment using miniconda. Adjust `requirements.txt` as per your needs, then install the packages within if necessary. Currently installing the packages in requirements.txt is not necessary, as no third-party libraries are used.
```
conda env create -n env_name python=3.10
conda activate env_name
```
### Quickstart
If not done, use your terminal to navigate to the root folder of the repository.<br>
Run `freq_run.sh` to run the script, if no input is submitted, it will run with the default input provided in `freq_config.json`
```bash
$ ./freq_run.sh

Enter document URL: https://www.gutenberg.org/cache/epub/16317/pg16317.txt
Enter start rank: 10
Enter end rank: 20
Top 10 to 20 words by frequency:
10: you (Frequency: 1467)
11: for (Frequency: 1340)
12: as (Frequency: 1202)
13: be (Frequency: 1181)
14: not (Frequency: 1166)
15: he (Frequency: 1075)
16: with (Frequency: 1035)
17: his (Frequency: 1029)
18: are (Frequency: 991)
19: i (Frequency: 956)
20: this (Frequency: 938)
```
Should you encounter permission issues, grant permission to run the script.
```bash
chmod +x freq_run.sh
```
### Alternative Methods of Running
If running the python script `wordfreq.py` directly, assuming you have navigated to the root folder:
```bash
$ python src/wordfreq.py https://www.gutenberg.org/cache/epub/16317/pg16317.txt 10 20

Top 10 to 20 words by frequency:
10: you (Frequency: 1467)
11: for (Frequency: 1340)
12: as (Frequency: 1202)
13: be (Frequency: 1181)
14: not (Frequency: 1166)
15: he (Frequency: 1075)
16: with (Frequency: 1035)
17: his (Frequency: 1029)
18: are (Frequency: 991)
19: i (Frequency: 956)
20: this (Frequency: 938)
```
### Parameter Adjustment
The parameters are available to adjust in the config file `freq_config.json` as well. 
- `url`: Direct link to the document
- `start_rank`: Integer. The highest rank for the printed list of word frequency to begin from
- `end_rank`: Integer. The lowest rank for the printed list of word frequency to end with<br>
Here is an example of the format of `freq_config.json`:
```
[
    {
        "url":"https://www.gutenberg.org/cache/epub/16317/pg16317.txt",
        "start_rank":10,
        "end_rank":20
    }
]
```
Note: In the event that `start_rank` input is larger than `end_rank` input, only the `start_rank`th entry will be printed.<br>
Example:
```bash
$ ./freq_run.sh

Enter document URL: 
Enter start rank: 25
Enter end rank: # end_rank default is 20, as per freq_config.json

Top 25 to 25 words by frequency:
25: your (Frequency: 835)
```
Example 2 (Triggering via python script):
```bash
$ python src/wordfreq.py '' 25 21
OR
$ python src/wordfreq.py '' 25 # 3rd argument will default to 20

Top 25 to 25 words by frequency:
25: your (Frequency: 835)
```