# Now, let's read the records from the json file
import json

import pandas as pd

with open('news_records_test.json', 'r') as f:
    loaded_records = json.load(f)

print(loaded_records[10])