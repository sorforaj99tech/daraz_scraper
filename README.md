# Daraz Scraper

A Python-based web scraping application that extracts product names and prices from Daraz Bangladesh using Selenium WebDriver.

## Overview

Daraz Scraper is an automation-based web scraping project developed with Python and Selenium. It allows users to provide a Daraz product link and automatically retrieve product information, including the product name and price.

## Features

- Accepts product links as user input
- Automates browser interaction using Selenium
- Extracts product names
- Retrieves product prices
- Supports headless Chrome browsing
- Automatically closes the browser after execution

## Technologies Used

- Python
- Selenium WebDriver
- Google Chrome
- ChromeDriver

## Project Structure

```text
daraz_scraper/
│
├── env/
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/sorforaj99tech/daraz_scraper.git
cd daraz_scraper
```

**2. Create a virtual environment**

```bash
python -m venv env
```

**3. Activate the environment**

Windows:

```bash
env\Scripts\activate
```

**4. Install dependencies**

```bash
pip install -r requirements.txt
```

**5. Run the application**

```bash
python main.py
```

## Usage

1. Run the application.
2. Enter a Daraz Bangladesh product URL when prompted.
3. The application retrieves and displays the product name and price.

## Requirements

- Python 3.10 or later
- Google Chrome
- Selenium WebDriver

## Author

**Sorforaj Ahmed**