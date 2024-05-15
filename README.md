# py_scripts
Python scripts for multiple purposes. Currently in progress: Text Generation with LLM, Word Frequency in Documents.
## Pre-requisites
- [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/)
## Text Generation with LLM
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
        "temperature":0.1
    }
]
```