import requests
from bs4 import BeautifulSoup
import smtplib

# Define the Amazon URL and user agent header
url = "https://www.amazon.com/Fallout-Game-Year-PC-video/dp/B074NJ39WX/ref=sr_1_3?crid=2LV7HDAWWNZHR&keywords=fallout+4+pc+digital+download&qid=1692423282&sprefix=fallout+4+pc+digital+download%2Caps%2C98&sr=8-3"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# Get the Amazon product page
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "lxml")

# Extract the product title and price
title = soup.find(id="productTitle").get_text().strip()
price_element = soup.find(class_="a-offscreen")
price = float(price_element.get_text().split("$")[1])

# Define the threshold price
BUY_PRICE = 25

# Compare the price with the threshold and send an email alert if needed
if price < BUY_PRICE:
    message = f"{title} is now ${price:.2f}"
    
    # Set up the SMTP server and send email
    smtp_server = "your_smtp_server_here"
    smtp_port = 587
    your_email = "your_email@example.com"
    your_password = "your_email_password"
    
    with smtplib.SMTP(smtp_server, port=smtp_port) as connection:
        connection.starttls()
        connection.login(your_email, your_password)
        connection.sendmail(
            from_addr=your_email,
            to_addrs=your_email,
            subject="Amazon Price Alert!",
            msg=f"Subject: Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
