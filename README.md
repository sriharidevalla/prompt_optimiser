# Prompt Perfect Clone

This repository contains a small clone of a prompt optimization tool inspired by the Prompt Perfect extension. The script provides a command-line interface to rewrite a user prompt with additional instructions aimed at producing better responses from language models. The new version supports custom instruction profiles and different response tones.

## Usage

Run the script with a prompt as an argument:

```bash
python3 main.py "Write a short story about space exploration"
```

If no prompt is provided on the command line, the script will ask for it interactively.

You can choose a response tone or load a custom instruction profile:

```bash
python3 main.py "Summarise the plot of Hamlet" --tone creative
python3 main.py "Explain quantum computing" --profile profile_example.json --output-file optimized.txt
```

`profile_example.json` shows how you can define your own base instructions and
tone-specific guidance.

## Output Example

```
$ python3 main.py "Write a poem about the ocean" --tone creative
Please respond to the following prompt with a detailed and well-structured answer.
Prompt: Write a poem about the ocean.

Instructions for the response:
- Use clear and concise language
- Provide examples when relevant
- Structure the response in short paragraphs
- Feel free to use expressive language and imagery.
- Incorporate metaphors or analogies where appropriate.
```

The script has no external dependencies and should work with any Python 3 installation.
