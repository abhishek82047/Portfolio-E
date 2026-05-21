import re
import os

css_path = 'c:/Users/abhis/OneDrive/Desktop/ALLPORT/PortfolioSite/css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# SAFE Minification
# 1. Remove comments
css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
# 2. Reduce multiple whitespaces to a single space
css = re.sub(r'\s+', ' ', css)
# 3. We will NOT strip spaces around operators to prevent breaking calc() or other CSS functions.
# However, we can safely strip spaces around semicolons, commas, and braces.
css = re.sub(r'\s*([\{\}\;\,\,])\s*', r'\1', css)
# Fix for empty rules
css = css.replace(';}', '}')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css.strip())

print("CSS safely minified.")
