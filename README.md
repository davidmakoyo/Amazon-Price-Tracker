# Amazon Price Tracker

Amazon Price Tracker is a Python script that automates real-time price monitoring for a specific Amazon product. It utilizes web scraping techniques, along with the BeautifulSoup library, to extract product information from an Amazon product page. When the product price falls below a predefined threshold, the script sends an email alert using the smtplib library.

## Features

- **Real-Time Price Monitoring:** The script fetches the product information, including its title and price, by utilizing web scraping techniques with the BeautifulSoup library.

- **Threshold-Based Alert:** The script compares the current price of the product with a predefined threshold price. If the product's price drops below the threshold, the script triggers an email alert.

- **Email Notification:** The script uses the smtplib library to send an email alert to the specified email address, providing information about the product and its current price.

## Usage

1. Replace the placeholders in the script with your Amazon product URL, SMTP server details, email address, and password.
2. Set the desired threshold price using the `BUY_PRICE` variable.
3. Run the script using a Python interpreter: `python amazon_price_tracker.py`.

## Example

Suppose you want to track the price of a specific Amazon product. You can configure the script with the product URL, desired threshold price, and email details. Once set up, the script will periodically fetch the product's price and send you an email notification if the price falls below the specified threshold.

## Dependencies

- [requests](https://pypi.org/project/requests/): For making HTTP requests to fetch the product page.
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/): For parsing HTML content and extracting relevant information.
- [smtplib](https://docs.python.org/3/library/smtplib.html): For sending email alerts.

