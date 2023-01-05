import datetime
import json
import os
from base64 import b64decode
from pathlib import Path

import typer
from dotenv import load_dotenv

import openai

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

DATA_DIR = Path.cwd() / "responses"
IMG_DIR = Path.cwd() / "images"
DATA_DIR.mkdir(exist_ok=True)
IMG_DIR.mkdir(exist_ok=True)

def img_converter(full_filename: Path):
    with open(full_filename, mode="r", encoding="utf-8") as file:
        response = json.load(file)

    for index, image_dict in enumerate(response["data"]):
        image_data = b64decode(image_dict["b64_json"])
        image_file = IMG_DIR / f"{full_filename.name}-{index}.png"
        with open(image_file, mode="wb") as png:
            png.write(image_data)
        typer.echo(f"Image created at {image_file}")

def main(description: str):
    typer.echo(f"Description received {description}, making request")
    time_now = datetime.datetime.now()
    file_name = time_now.strftime("%Y-%m-%d_%H%M%S")
    full_filename = DATA_DIR / f"{file_name}.json"
    
    response = openai.Image.create(
        prompt=description,
        n=1,
        size="256x256", 
        response_format="b64_json",
    )

    typer.echo(f"Response received, saving json at {full_filename}")
    with open(full_filename, mode="w", encoding="utf-8") as file:
        json.dump(response, file)

    img_converter(full_filename)
    
    
if __name__ == "__main__":
    typer.run(main)