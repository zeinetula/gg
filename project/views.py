"""
Run this script to seed the database with sample data from Lab 5.

Usage:
    python manage.py shell < api/seed.py
"""
from api.models import Category, Product

# Clear existing data
Product.objects.all().delete()
Category.objects.all().delete()

# Create categories (from Lab 5)
smartphones = Category.objects.create(name="Smartphones")
laptops = Category.objects.create(name="Laptops")
headphones = Category.objects.create(name="Headphones")
tablets = Category.objects.create(name="Tablets")

# Smartphones
Product.objects.create(name="iPhone 15 Pro", price=599990, description="Apple iPhone 15 Pro 256GB", count=10, is_active=True, category=smartphones)
Product.objects.create(name="Samsung Galaxy S24", price=449990, description="Samsung Galaxy S24 Ultra 256GB", count=15, is_active=True, category=smartphones)
Product.objects.create(name="Xiaomi 14", price=299990, description="Xiaomi 14 Pro 512GB", count=20, is_active=True, category=smartphones)
Product.objects.create(name="Google Pixel 8", price=349990, description="Google Pixel 8 Pro 128GB", count=8, is_active=True, category=smartphones)
Product.objects.create(name="OnePlus 12", price=379990, description="OnePlus 12 256GB", count=12, is_active=True, category=smartphones)

# Laptops
Product.objects.create(name="MacBook Air M3", price=749990, description="Apple MacBook Air 15 M3 256GB", count=5, is_active=True, category=laptops)
Product.objects.create(name="ASUS VivoBook 15", price=329990, description="ASUS VivoBook 15 i5 16GB 512GB", count=18, is_active=True, category=laptops)
Product.objects.create(name="Lenovo IdeaPad 3", price=279990, description="Lenovo IdeaPad 3 15 Ryzen 5", count=22, is_active=True, category=laptops)
Product.objects.create(name="HP Pavilion 14", price=399990, description="HP Pavilion 14 i7 16GB 512GB SSD", count=7, is_active=True, category=laptops)
Product.objects.create(name="Acer Aspire 5", price=249990, description="Acer Aspire 5 i5 8GB 256GB", count=14, is_active=True, category=laptops)

# Headphones
Product.objects.create(name="AirPods Pro 2", price=129990, description="Apple AirPods Pro 2nd Gen USB-C", count=30, is_active=True, category=headphones)
Product.objects.create(name="Sony WH-1000XM5", price=179990, description="Sony WH-1000XM5 Wireless ANC", count=12, is_active=True, category=headphones)
Product.objects.create(name="Samsung Galaxy Buds2 Pro", price=89990, description="Samsung Galaxy Buds2 Pro ANC", count=25, is_active=True, category=headphones)
Product.objects.create(name="JBL Tune 770NC", price=49990, description="JBL Tune 770NC Wireless", count=35, is_active=True, category=headphones)
Product.objects.create(name="Marshall Major IV", price=69990, description="Marshall Major IV Bluetooth", count=16, is_active=True, category=headphones)

# Tablets
Product.objects.create(name="iPad Air M2", price=449990, description="Apple iPad Air 11 M2 128GB", count=9, is_active=True, category=tablets)
Product.objects.create(name="Samsung Galaxy Tab S9", price=399990, description="Samsung Galaxy Tab S9 FE 128GB", count=11, is_active=True, category=tablets)
Product.objects.create(name="Xiaomi Pad 6", price=199990, description="Xiaomi Pad 6 128GB", count=20, is_active=True, category=tablets)
Product.objects.create(name="Lenovo Tab P12", price=249990, description="Lenovo Tab P12 128GB", count=13, is_active=True, category=tablets)
Product.objects.create(name="Huawei MatePad 11", price=179990, description="Huawei MatePad 11 128GB", count=17, is_active=True, category=tablets)

print(f"Seeded {Category.objects.count()} categories and {Product.objects.count()} products.")
