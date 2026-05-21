import re

html_path = 'c:/Users/abhis/OneDrive/Desktop/ALLPORT/PortfolioSite/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

imgs = re.findall(r'<img[^>]*>', html)
for img in imgs:
    if 'loading="lazy"' not in img:
        print('EAGER:', img)
