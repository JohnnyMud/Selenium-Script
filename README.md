# Sports Props Web Scraper
This is a Python-based web scraping project designed to extract player prop data from a sports betting platform (app.prizepicks.com). The script uses Selenium for browser automation, processes the data into a Pandas DataFrame, and stores the results into a PostgreSQL database. This project is ideal for building an up-to-date sports props database or feeding live projections into a data pipeline.
## Features
- Selenium Automation: Connects to a Chrome debugging session for secure manual login.
- Data Extraction: Scrapes player names, prop types, and projection values.
- Data Enrichment: Adds scrape date for tracking and filtering.
- Database Integration: Inserts cleaned data into a PostgreSQL table for future analysis.
## Technologies Used
- Python 3
- Selenium
- Pandas
- PostgreSQL (via psycopg2)
