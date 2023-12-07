This repo contains a script that uses sample stock and movement database to generate a result database (on `data` folder), reporting inital and final values for the day, and how much entry or exit happened in the stock.

# How it works?
The script uses python and pandas to read and analyze the sample.
- read csv;
- group and save movement table by item code in an "item" set;
- run through each new "item" set;
  - gets initial value and quantity from stock database using item code;
  - group and save "table" set by date in a new "date" set;
  - run through each new "date" set;
    - gets timestamp from date set;
    - update entry quantity and value and leave quantity and value;
    - calculates end quantity and value;
    - saves result;
    - replace init quantity and value with the end quantity and value (the next day's initial values ​​are the end of the previous one)
- saves results in csv

# How to test it?
Simple, delete `result.csv` from `data` and run `generate_csv.py`. You will need pandas, recommended to create a venv.