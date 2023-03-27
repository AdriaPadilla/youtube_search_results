# YouTube Search Results Tracker

This script is created to study YouTube search results in one (or more) querie/s. Through YouTube API, it will make a request and save the data in an .xlsx file.

The purpose of this script is entirely academic, and it has been created to observe the evolution of search results over time.

The script can be automated using CRON on a Linux system.

The data can be dumped to a MYSQL database, by uncommenting and filling the fields in the export.py file.

### Required Modules
```
pandas
pymsql # Only if MSQL Dump
sqlalchemy # Only if MSQL Dump
openpyxl # Needed for .xlsx dataframe export. Not needed if use .to_csv() 
google-api-python-client
```

## Define query and max results

on **main.py**:
```python
queries = ["query_1", "query_2", "query_n"]
max_results = n # Use integer number calculated within your YouTube API Quota
```

## Export file
- If use .xslx export. filename will be "%m-%d-%Y-%H-%M-%S"-query.xlsx"
- You can change this on line 65 in export.py
