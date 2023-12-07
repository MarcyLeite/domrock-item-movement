This repo contains a script that uses sample stock and movement database to generate a result database (on `data` folder), reporting inital and final values for the day, and how much entry or exit happened in the stock.

# How it works?
The script uses python and pandas to read and parse the sample.
- read csvs;
- group and save movement table by item code in a "item" set;
- run trough each new "item" set;
  - gets initial value and quantity from stock database using code;
  - group and save "table" set by date in a new "date" set;
  - run trough each new "date" set;
    - gets timestamp from date set;
    - increment entry quantity and value and leave quantity and value;
    - calculates end quantity and value;
    - saves result;
    - replace init quantity and value to end quantity and value (init values of the next day are the end of the previous one)
- saves results in csv