# Bookstore Scraper

## Overview

Bookstore Scraper is a Python application that collects book information from the Books to Scrape website.

The scraper extracts product details, pricing information, category data, and product images.
The collected data is then exported to CSV files for further analysis.

This project was completed as part of the OpenClassrooms Python Developer program.

## Features

- Extract product data from Books to Scrape
- Scrape complete book categories
- Scrape the entire website catalog
- Download product images
- Export collected data to CSV files

## Tech Stack

- Python 3
- Requests
- Beautiful Soup 4
- CSV
- urllib

## Installation

### Clone the Repository

- `git clone https://github.com/fabroyer/bookstore-scraper.git`
- `cd bookstore-scraper`

### Create and Activate Virtual Environment

Windows:
```bash
python -m venv env
env\Scripts\activate
```

Mac/Linux:
```bash
python -m venv env
source env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

```bash
python scraping_website.py
```

Output files are generated in:

- `Fichier_CSV/` for CSV exports
- `Images/` for downloaded product images
