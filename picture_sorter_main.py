import base64
import json
import os
import subprocess

import requests

import config


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


folder_path = config.folder_path  # user input
cp_or_mv = config.cp_or_mv

items = os.listdir(folder_path)
for item in items:
    try:
        image_path = f"{folder_path}/{item}"
        base64_image = encode_image(image_path)

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llava",
                "prompt": config.promt,
                "images": [base64_image],
                "stream": False,
            },
        )

        finding_object = config.finding_object
        finding_object_words = [f" {word} " for word in finding_object.split()]
        finding_object_words_with_sign = []
        for word in finding_object_words_with_sign:
            finding_object_words.append(f"{word}.")
            finding_object_words.append(f"{word},")
            finding_object_words.append(f"{word}'")
        finding_object_words = finding_object_words + finding_object_words_with_sign
        print(json.loads(response.text)["response"])
        for word in finding_object_words:
            if word in json.loads(response.text)["response"]:
                os.makedirs(f"{folder_path}/sorted", exist_ok=True)
                subprocess.run(
                    f"{cp_or_mv} '{folder_path}/{item}' '{folder_path}/sorted/'",
                    shell=True,
                    capture_output=True,
                    text=True,
                )
                print(f"object {word} is found")
                break
            else:
                print(f"object {word} is not found")
    except Exception as e:
        print(e)
