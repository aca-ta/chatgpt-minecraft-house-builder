# ChatGPT Minecraft House Builder
This Python script demonstrates how to use OpenAI's ChatGPT API to generate Python code for building a house in Minecraft using the mcpi library.

## Usage
The script will first send a message to the ChatGPT API, asking it to generate Python code for building a house in Minecraft using the mcpi library. The API will then return the generated code, which will be executed in the script to build the house in your Minecraft world.

Make sure your Minecraft world is running on the same machine, and that you have established a connection using the following line in your script:

```bash
export OPENAI_API_KEY="your-api-key"
poetry run python main.py
```
