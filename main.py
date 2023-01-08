import datetime
import json
import os
from base64 import b64decode
from pathlib import Path
from typing import Callable

import typer
from dotenv import load_dotenv

import openai

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

RESPONSES_DIR = Path.cwd() / "responses"
IMG_DIR = Path.cwd() / "images"
RESPONSES_DIR.mkdir(exist_ok=True)
IMG_DIR.mkdir(exist_ok=True)

class ResponseHandler:
    def __init__(self, description: str) -> None:
        
        file_name = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
        full_filename = RESPONSES_DIR / f"{file_name}.json"
        self.full_filename = full_filename
        self.description = description
        
    def handler(self, create) -> Callable:
        handler_dict = {
            "image": "image_handler",
            "text": "text_handler"
        }
        hand = handler_dict.get(create, "image_handler")
        return getattr(self, hand) # type:ignore

    def image_handler(self) -> None:
        typer.secho(f"Image Handler selected", fg=typer.colors.GREEN)
        response = openai.Image.create(
            prompt=self.description,
            n=1,
            size="256x256", 
            response_format="b64_json",
        )
        self.save_response(self.full_filename, response)
        self.img_converter(self.full_filename)
        
    def text_handler(self) -> None:
        typer.secho(f"Text Handler selected", fg=typer.colors.GREEN)
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=self.description,
            temperature=0.7,
            max_tokens=500,
            top_p=0.3,
            frequency_penalty=0.5,
            presence_penalty=0
            )
        self.save_response(self.full_filename, response)
        self.text_extractor(self.full_filename)
    
    @staticmethod
    def text_extractor(full_filename) -> None:
        with open(full_filename, mode="r", encoding="utf-8") as file:
            response = json.load(file)
            text = response['choices'][0]["text"].replace("\n", "")
            typer.secho(text, fg=typer.colors.BRIGHT_BLUE)
    
    @staticmethod
    def img_converter(full_filename: Path)-> None:
        with open(full_filename, mode="r", encoding="utf-8") as file:
            response = json.load(file)

        for index, image_dict in enumerate(response["data"]):
            image_data = b64decode(image_dict["b64_json"])
            image_file = IMG_DIR / f"{full_filename.name}-{index}.png"
            with open(image_file, mode="wb") as png:
                png.write(image_data)
            typer.secho(f"Image created at {image_file}", fg=typer.colors.GREEN)
    
    @staticmethod
    def save_response(full_filename, response) -> None:
        typer.secho(f"Response received, saving json at {full_filename}, fg=typer.colors.GREEN")
        with open(full_filename, mode="w", encoding="utf-8") as file:
            json.dump(response, file)
        
def main(
    create: str = typer.Option("Image", help="Enter image for image creation or text for text creation.", rich_help_panel="Customization and Utils"),
    description: str = typer.Option("", help="Enter here the description for your request, long descriptions are better than short ones.", rich_help_panel="Customization and Utils"), 
    ):
    # create = "Image"
    # description = "Create 3d image from big bang, inside a glass of water with light background"
    # create = "text"
    # description = "Create LinkdIn clickbait post title about an script in python to help users use OpenAI"
    
    typer.secho(f"Description received {description}, making request", fg=typer.colors.GREEN)
    create = create.lower()
    resp_handler = ResponseHandler(description=description)
    handler = resp_handler.handler(create)
    handler()
    
    
if __name__ == "__main__":
    typer.run(main)