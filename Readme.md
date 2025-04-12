# All to OpenAI-Compatible-API  

This project introduces several methods for converting different types of model servers into an OpenAI-Compatible API.  

If you find this project useful, please consider giving it a star 🌟 to show your support 💖!  

Sure! Here's the polished version with a checklist:

**Current Progress:**

- [x] Support for POST-request-based LLM services  
- [x] Support for local LLM models using vllm

## API Test

Before explaining how to convert model servers to the OpenAI-Compatible API server, we provide two testing methods.  

### 1. Python Package

A simple test function is provided in `test_openai_api.py`.  

### 2. curl

```bash
curl "http://localhost:8001/v1/chat/completions" \
    -H "Content-Type: application/json" \
    -d '{
        "model": "model_name",
        "messages": [
            {
                "role": "user",
                "content": "Who are you?"
            }
        ]
    }'
```

For additional test parameters, refer to the official documentation: [https://platform.openai.com/docs/quickstart](https://platform.openai.com/docs/quickstart)  

## 1. LLM Based on POST Requests  

In `post_to_openai_api.py`, we implement functionality to convert any POST request into an OpenAI-Compatible API service that supports asynchronous requests.  

First, modify all lines in `post_to_openai_api.py` containing the `"ToChange"` tag, including the URL, headers, and response handling method.  

After that, run the following command to start the service:  

```bash
python post_to_openai_api.py --port 8001
```

## 2. Local LLM  

We highly recommend using `vllm`'s built-in proxy service.  

### Installing vllm

Follow these steps for a quick installation:  

```bash
conda create -n vllm python=3.12 -y
conda activate vllm
pip install vllm
```

If the installation fails, refer to the official guide: [https://docs.vllm.ai/en/stable/getting_started/installation/gpu/index.html](https://docs.vllm.ai/en/stable/getting_started/installation/gpu/index.html)  

### Starting the Service

Once `vllm` is installed, use the following command to deploy the service:  

```bash
bash local_to_openai_api.sh
```

For detailed configuration options, refer to the official documentation: [https://docs.vllm.ai/en/stable/serving/openai_compatible_server.html](https://docs.vllm.ai/en/stable/serving/openai_compatible_server.html)  