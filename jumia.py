from bs4 import BeautifulSoup
import requests


url = "https://www.jumia.co.ke/catalog/?q=tvs"

response = requests.get(url)


if response.status_code == 200:
    
    soup = BeautifulSoup(response.text, "html.parser")


    products = soup.find_all("article", class_="prd _fb col c-prd")

    
    for product in products:
        brand = product.find("h3", class_="name").text.strip() if product.find("h3", class_="name") else "N/A"
        price = product.find("div", class_="prc").text.strip() if product.find("div", class_="prc") else "N/A"
        discount = product.find("div", class_="tag _dsct").text.strip() if product.find("div", class_="tag _dsct") else "N/A"
        rating = product.find("div", class_="stars _s").get("data-rating") if product.find("div", class_="stars _s") else "N/A"

    
        print(f"Brand: {brand}")
        print(f"Price: {price}")
        print(f"Discount: {discount}")
        print(f"Rating: {rating}")
        print("*" * 40)
else:
    print("Failed to retrieve the page. Status code:", response.status_code)
