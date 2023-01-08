# Open AI API consumer

## What's Open AI?

Is highly autonomous systems that outperform humans at most economically valuable work—benefits all of humanity.

Using this script it's possible to describe an image and the AI will create an image based on your description or use it to create texts, titles or own names.
These text-to-image systems use a range of complex technology such as deep learning algorithms and generative adversarial networks (GANs)

## Why use it?

First of all I want try OpenAI, using [Typer](https://typer.tiangolo.com/) to build a friendly command line and consuming [OpenAI API](https://github.com/openai/openai-python). Second, I read that OpenAI is winning digital contests around the world -> [link](https://www.nytimes.com/2022/09/02/technology/ai-artificial-intelligence-artists.html). So, why not?

Let's start!

## Requirements

- python 3.8+ installed
- terminal to run commands
- IDE if you need to edit any code
- know how to clone this repo

Create virtual environment and install requirements

**On Linux**

```Shell
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**On Windows**

```Shell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### Your OpenAI API Key

To make successful calls to the Open AI API, you will need to register to Open API and create a new API Key by clicking on the dropdown menu on your profile and selecting [View API key](https://beta.openai.com/account/api-keys). Create a `.env` file and copy to it: `OPENAI_API_KEY="<your-key-value-here>"`

After everything installed and set it's possible to start using it.

## How It Works

At the terminal, type: `python main.py --help` and the output should be something like this:

```Shell
Usage: main.py [OPTIONS]

╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                                                                                    │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Customization and Utils ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --create             TEXT  Enter image for image creation or text for text creation. [default: Image]                                                                          │
│ --description        TEXT  Enter here the description for your request, long descriptions are better than short ones.                                                          │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```

Great! The code is working and the command line is responsively, let's try to create some image.

At the terminal type: `python main.py image "Space Opera Theater"`, wait for the outputs in the command line and check when the image has been saved: `Image created at /... .png`

 <p align="center">
  <img src="./images/2023-01-05_100416.json-0.png" alt="Size Limit CLI" width="512">
</p>

You will win the digital image contest?
