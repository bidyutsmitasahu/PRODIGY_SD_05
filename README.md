# Amazon Product Scraper 🛒🕷️



**Professional web scraper** that extracts **product names, prices, ratings, reviews & URLs** from Amazon search results and exports to **CSV** for instant analysis. Perfect for price tracking & market research!

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📦 **Complete Data** | Name, price, rating, reviews count, product URL |
| 📊 **CSV Export** | Ready for Excel, Pandas, Google Sheets |
| 🔍 **Multi-Page** | Scrapes 2+ pages of search results |
| ⏱️ **Rate Limited** | Polite delays prevent blocking |
| 🛡️ **Error Handling** | Continues despite individual failures |
| 🎯 **Interactive** | Console UI - just enter search term! |

## 🛒 Sample CSV Output

| name | price | rating | reviews | url |
|-----|-------|--------|---------|-----|
| Apple AirPods Pro (2nd Gen) | $249 | 4.8 | 125K+ ratings | https://amazon.com/... |
| Sony WH-1000XM5 Headphones | $399 | 4.7 | 89K+ ratings | https://amazon.com/... |
| Bose QuietComfort 45 | $329 | 4.6 | 45K+ ratings | https://amazon.com/... |

## 🚀 Quick Start

```bash
# 1. Clone & install
git clone https://github.com/yourusername/amazon-scraper.git
cd amazon-scraper
pip install -r requirements.txt

# 2. Run scraper
python amazon_scraper.py
```

```
Enter product search term: wireless headphones
Enter pages (default 2): 
🚀 Scraping 'wireless headphones' (2 pages)...
💾 Saved 24 products to amazon_products.csv
🎉 SUCCESS!
```

## 📦 Installation

```bash
pip install requests beautifulsoup4 lxml
```

**Python 3.6+ required** - No other dependencies!

## 🎬 Live Demo

```
🛒 Amazon Product Scraper
==================================================
Enter product search term (e.g., 'laptop'): wireless headphones

🚀 Starting scrape for 'wireless headphones' (2 pages)...
🕷️ Scraping page 1: https://amazon.com/s?k=wireless+headphones&page=1
✅ Found 12 products on page 1
🕷️ Scraping page 2: https://amazon.com/s?k=wireless+headphones&page=2
✅ Found 12 products on page 2

📊 Sample:
1. Apple AirPods Pro... | $249 | 4.8★
2. Sony WH-1000XM5... | $399 | 4.7★
3. JBL Tune Flex... | $99 | 4.5★
```

## 🛠️ How It Works

```python
# Core extraction logic
def _extract_product_info(self, element):
    return {
        'name': name_elem.get_text(strip=True),
        'price': price_elem.get_text(strip=True), 
        'rating': rating.split()[0],
        'reviews': reviews_text,
        'url': full_product_url
    }
```

1. **Session Management** - Persistent cookies & realistic headers
2. **Dynamic Parsing** - Handles Amazon's complex HTML structure
3. **Pagination** - Automatic multi-page scraping
4. **CSV Export** - Clean, structured output

## 📁 Project Structure

```
amazon-scraper/
├── amazon_scraper.py       # Main scraper (220 LOC)
├── amazon_products.csv     # Sample output
├── requirements.txt        # pip install -r requirements.txt
├── README.md              # This file
├── demo_screenshot.png    # Visual demo
└── LICENSE                # MIT License
```

## 🔧 Advanced Usage

```python
# Programmatic usage
scraper = AmazonProductScraper()
products = scraper.scrape_products("4k tv", max_pages=3)
scraper.save_to_csv(products, "tv_prices.csv")

# Pandas integration
import pandas as pd
df = pd.read_csv("amazon_products.csv")
print(df.nlargest(10, "rating"))
```

## 📈 Post-Processing Examples

```python
# Price analysis
df['price_num'] = df['price'].str.replace('$', '').astype(float)
print(f"Avg price: ${df['price_num'].mean():.2f}")

# Top rated products
top_rated = df[df['rating'] != 'N/A'].nlargest(5, 'rating')
```

## ⚠️ Important Notes

- 🛡️ **Educational Use Only** - Respect Amazon ToS
- ⏱️ **Rate Limited** - 1-3s delays between requests
- 🔄 **Dynamic HTML** - May need updates if Amazon changes layout
- 🌍 **Global Ready** - Works with amazon.com, .co.uk, .in, etc.

## 🤝 Contributing

1. Fork repository
2. Create feature branch (`git checkout -b feature/add-walmart`)
3. Commit changes (`git commit -am 'Add Walmart scraper'`)
4. Push & submit PR

## 📄 License

[MIT License](LICENSE) - Free for personal & commercial use!

## 🚀 Next Steps

- [ ] Add Walmart/Flipkart support
- [ ] Image download capability
- [ ] Price history tracking
- [ ] REST API endpoints

***

