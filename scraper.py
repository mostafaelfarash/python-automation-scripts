import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_data():
    url = "https://books.toscrape.com/"
    
    print("[*] جاري الاتصال بالموقع وسحب البيانات...")
    response = requests.get(url)
    
    if response.status_code != 200:
        print("[!] حدث خطأ في الاتصال بالموقع.")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    data = []
    books = soup.find_all('article', class_='product_pod')
    
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        price_clean = price.replace('Â', '').strip()
        
        data.append({
            'Book Title': title,
            'Price': price_clean
        })
    
    df = pd.DataFrame(data)
    excel_file = "scraped_books_data.xlsx"
    df.to_excel(excel_file, index=False)
    
    print(f"[+] تم سحب البيانات بنجاح وحفظها في الملف: {excel_file}")

if __name__ == "__main__":
    scrape_data()