"""Main module to get battle details of a Pokemon from Pokemon GO"""

import os
from argparse import ArgumentParser
from pathlib import Path

import filetype

from dotenv import load_dotenv
import easyocr
from openai import OpenAI

from service_const import SYSTEM_CONTENT

load_dotenv()  # Load variables from .env
api_key = os.getenv("OPENAI_API_KEY")


def argument_parser():
    """Defining arguments"""
    parser = ArgumentParser()
    parser.add_argument(
        "-i",
        "--image",
        help="Path of the screenshot of Pokemon's details",
        required=True,
    )
    return parser.parse_args()


def extract_text(img_path):
    """
    Function to extract the text from image"
    image_path: Path of the screenshot from Pokemon's details in Pokemon GO
    """
    reader = easyocr.Reader(["en"])
    image_text = reader.readtext(img_path)
    result = ""
    for detected_character in image_text:
        result += detected_character[1] + " "
    return result


def get_information_from_openai(text):
    """
    Function to get Pokemon's information asking to OpenAI
    text: Text extracted from Pokemon's details in Pokemon GO
    """
    client = OpenAI(api_key=api_key)
    chat_response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": SYSTEM_CONTENT},
            {"role": "user", "content": text},
        ],
        response_format={"type": "json_object"},
    )
    return chat_response.model_dump()["choices"][0]["message"]["content"]


def check_if_image(file_path):
    """Confirm if the string passed is an image"""
    if not file_path:
        raise Exception("Image argument is not valid")
    if Path(file_path).is_file():
        if not filetype.is_image(file_path):
            raise Exception("The file is not an image")
    else:
        raise FileNotFoundError("The file doesn't exist")
    return True


if __name__ == "__main__":
    args_parser = argument_parser()
    if check_if_image(args_parser.image):
        extracted_text = extract_text(args_parser.image)
        response = get_information_from_openai(extracted_text)
        print(response)
