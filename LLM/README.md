## Setup
1. Download model:
```bash
ollama pull llama3
```

2. Check models list:
```bash
ollama list
```

3. Create `dataset.jsonl`:
```jsonl
{"prompt": "<prompt>", "response": "<response>"}
```

4. Create `Modelfile`:
```modelfile
FROM llama3:8b-instruct

SYSTEM """
You are a helpful assistant fluent in English and Tagalog.
Your task is to translate English sentences into Tagalog accurately and naturally.
"""

TEMPLATE """
User: {{ .Prompt }}
Assistant:
"""
```

5. Fine tune the model:
```bash
ollama create <model-name> -f Modelfile
```

6. Run model:
```bash
ollama run <model-name>
```

## Commands
```bash
ollama rm <model-name> # delete model
ollama list            # check existing models
```

## Tokenization
1. Install SentencePiece:
```bash
pip install sentencepiece   
```