import re

html_path = 'c:/Users/abhis/OneDrive/Desktop/ALLPORT/PortfolioSite/index.html'
css_path = 'c:/Users/abhis/OneDrive/Desktop/ALLPORT/PortfolioSite/css/style.css'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Remove the existing preload and stylesheet links for style.css
html = html.replace('<link rel="preload" href="css/style.css" as="style">', '')
html = html.replace('<link rel="stylesheet" href="css/style.css">', f'<style>\n{css}\n</style>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("CSS inlined successfully!")
