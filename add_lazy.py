import re

html_path = 'c:/Users/abhis/OneDrive/Desktop/ALLPORT/PortfolioSite/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

def repl(m):
    img = m.group(0)
    if 'loading="lazy"' in img or 'hero_char.webp' in img:
        return img
    return img.replace('<img ', '<img loading="lazy" ')

html = re.sub(r'<img[^>]*>', repl, html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Lazy loading added to eager images.")
