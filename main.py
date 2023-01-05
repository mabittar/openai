import typer
import os
import json
import os
import openai
import datetime

from pathlib import Path
from dotenv import load_dotenv
from base64 import b64decode
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

def main(definition: str):

    time_now = datetime.datetime.now()
    file_name = time_now.strftime("%Y-%m-%d_%H%M%S")
    full_filename = DATA_DIR / f"{file_name}.json"
    response = openai.Image.create(
        prompt=definition,
        n=1,
        size="1024×1024",
        response_format="b64_json",
    )

    with open(full_filename, mode="w", encoding="utf-8") as file:
        json.dump(response, file)

    img_converter(full_filename)
if __name__ == "__main__":
    typer.run(main)