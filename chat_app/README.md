# Local LLM Chatbot

A chat-based AI application built with Python that runs entirely on your local machine. Designed for privacy-first AI interactions with no API costs, keeping your data secure while giving you full control over your code and models.

# Tech stack used
Python: The core programming language that ties together all components of the project.

Ollama: A tool for running powerful language models like Llama and Mistral locally on your machine.

Streamlit: A Python framework that quickly transforms scripts into interactive web applications.

####  Setup with uv (Recommended)

[uv](https://github.com/astral-sh/uv) is a fast Python package installer and resolver.

1. Install uv, if not already installed:

```bash
pip install uv
```
2. Download Ollama from https://ollama.com/

3. Pull the model using command

```bash
   ollama pull llama3
```
4. Create and activate a virtual environment:

```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
5. Then, make a new folder for your project, open your terminal in that folder, and run

```bash
   uv add ollama streamlit
```
6. Install dependencies:

```bash
uv sync
```

4. Run the project (make sure you are in correct directory to run the command)

```bash
streamlit run app.py
```
### If you have python installed from various sources there can be conflict
### below commands can help resolved issues
```bash
which python
python -c "import sys; print(sys.executable)"
```
```bash
conda deactivate
```
```bash
rm -rf .venv/
```
```bash
uv venv --python /usr/Local/bin/python3.13
```
```bash
source .venv/bin/activate
```
```bash
uv sync
```

### Linting and Typing Check

There are no lint or type checks implemented.
