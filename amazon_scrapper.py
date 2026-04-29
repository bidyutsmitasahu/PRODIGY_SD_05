import requests
from bs4 import BeautifulSoup
import csv
import time
import random
from typing import List, Dict
import os

class AmazonProductScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        })
        self.base_url = "https://www.amazon.com"
    
    def scrape_products(self, search_query: str, max_pages: int = 2) -> List[Dict]:
        """Scrape product data from Amazon search results."""
        products = []
        page = 1
        
        while page <= max_pages:
            # Construct search URL
            url = f"{self.base_url}/s?k={search_query.replace(' ', '+')}&page={page}"
            print(f"🕷️ Scraping page {page}: {url}")
            
            try:
                response = self.session.get(url, timeout=10)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.content, 'html.parser')
                product_elements = soup.find_all('div', {'data-component-type': 's-search-result'})
                
                if not product_elements:
                    print("❌ No products found on this page")
                    break
                
                for element in product_elements[:12]:  # Top 12 products per page
                    product = self._extract_product_info(element)
                    if product:
                        products.append(product)
                
                print(f"✅ Found {len(product_elements[:12])} products on page {page}")
                
            except Exception as e:
                print(f"❌ Error on page {page}: {e}")
                break
            
            page += 1
            # Polite delay
            time.sleep(random.uniform(1, 3))
        
        return products
    
    def _extract_product_info(self, element) -> Dict:
        """Extract detailed info from single product element."""
        try:
            # Product name
            name_elem = element.find('h2', class_='a-size-mini') or element.find('span', class_='a-size-base-plus')
            name = name_elem.get_text(strip=True) if name_elem else "N/A"
            
            # Price
            price_elem = element.find('span', class_='a-price-whole')
            price = price_elem.get_text(strip=True) if price_elem else "N/A"
            
            # Rating
            rating_elem = element.find('span', class_='a-icon-alt')
            rating = rating_elem.get_text().split()[0] if rating_elem else "N/A"
            
            # Reviews count
            reviews_elem = element.find('span', class_='a-size-base')
            reviews = reviews_elem.get_text(strip=True) if reviews_elem else "N/A"
            
            # Link
            link_elem = element.find('a', class_='a-link-normal')
            link = self.base_url + link_elem['href'] if link_elem and link_elem.get('href') else "N/A"
            
            return {
                'name': name[:100],  # Truncate long names
                'price': price,
                'rating': rating,
                'reviews': reviews,
                'url': link
            }
            
        except Exception as e:
            print(f"⚠️ Error extracting product: {e}")
            return None
    
    def save_to_csv(self, products: List[Dict], filename: str = "amazon_products.csv"):
        """Save products to CSV file."""
        if not products:
            print("❌ No products to save!")
            return
        
        file_exists = os.path.exists(filename)
        
        with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['name', 'price', 'rating', 'reviews', 'url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            if not file_exists:
                writer.writeheader()
            
            writer.writerows(products)
        
        print(f"💾 Saved {len(products)} products to {filename}")

def main():
    scraper = AmazonProductScraper()
    
    print("🛒 Amazon Product Scraper")
    print("=" * 50)
    
    search_query = input("Enter product search term (e.g., 'laptop'): ").strip()
    if not search_query:
        search_query = "wireless headphones"
    
    max_pages = input("Number of pages to scrape (default 2): ").strip()
    max_pages = int(max_pages) if max_pages.isdigit() else 2
    
    print(f"\n🚀 Starting scrape for '{search_query}' ({max_pages} pages)...")
    print("⚠️  Respect Amazon's ToS - use responsibly!")
    
    products = scraper.scrape_products(search_query, max_pages)
    
    if products:
        scraper.save_to_csv(products)
        print(f"\n🎉 SUCCESS! Scraped {len(products)} products!")
        print("\n📊 Sample:")
        for i, p in enumerate(products[:3], 1):
            print(f"{i}. {p['name'][:50]}... | ${p['price']} | {p['rating']}★")
    else:
        print("😞 No products found. Try different search term.")

if __name__ == "__main__":
    main()