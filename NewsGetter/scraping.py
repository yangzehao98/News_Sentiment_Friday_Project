import json
import time

import numpy as np
import requests
from bs4 import BeautifulSoup

import pandas as pd

with open('news_records_test.json', 'r') as f:
    loaded_records = json.load(f)

urls = []
for record in loaded_records:
    urls.append(record['url'])

contents = []

for index, url in enumerate(urls):
    print(f"Fetching content from URL {index + 1}/{len(urls)}")
    # Fetch the content from the URL
    response = requests.get(url)
    content = response.content
    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(content, 'html.parser')

    first_div = soup.find('div')

    # Initialize an empty string to accumulate the content
    content_str = ""

    if first_div:
        # Find all <p> with class 'block core-block' within the first <div>
        blocks = first_div.find_all('p', class_='block core-block')
        # Concatenate the text of each <p> into the content_str
        for block in blocks:
            content_str += block.text + " "  # Adding a space for separation

    # Trim any excess whitespace from the final string
    content_str = content_str.strip()
    contents.append(content_str)
    # add a normal distribution random wait time
    wait_time = 1 + np.random.normal(0, 0.5)
    wait_time = max(1, wait_time)
    time.sleep(wait_time)


def update_jsons_and_save_to_single_file(json_list, string_list, key_to_update='content', output_filename='updated_jsons.json'):
    """
    Update a list of JSON objects with corresponding strings from another list and save all to a single JSON file.

    :param json_list: List of dictionaries representing JSON objects.
    :param string_list: List of strings to update the JSON objects with.
    :param key_to_update: The key in the JSON objects to be updated with the strings. Defaults to 'content'.
    :param output_filename: The filename for the single output JSON file. Defaults to 'updated_jsons.json'.
    """
    if len(json_list) != len(string_list):
        raise ValueError("The length of json_list and string_list must be the same.")

    updated_json_list = []  # Initialize an empty list to hold the updated JSON objects

    for json_obj, update_str in zip(json_list, string_list):
        # Update the JSON object with the corresponding string
        json_obj[key_to_update] = update_str
        # Append the updated JSON object to the list
        updated_json_list.append(json_obj)

    # Save the list of updated JSON objects to a single file
    with open(output_filename, 'w') as f:
        json.dump(updated_json_list, f, indent=4)

    print(f"Saved all updated JSON objects to {output_filename}")

update_jsons_and_save_to_single_file(loaded_records, contents, 'content',output_filename='news_data.json')


