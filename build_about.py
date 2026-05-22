import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract head
head_match = re.search(r'(<!DOCTYPE html>.*?<head>.*?</head>\s*<body>)', content, re.DOTALL)
head_part = head_match.group(1)

# Extract nav
nav_match = re.search(r'(<!-- NAV -->.*?)(<!-- MOBILE MENU -->)', content, re.DOTALL)
nav_part = nav_match.group(1)

# Extract mobile menu
mob_match = re.search(r'(<!-- MOBILE MENU -->.*?</div>)', content, re.DOTALL)
mob_part = mob_match.group(1)

# Extract about section
about_match = re.search(r'(<!-- ABOUT -->\s*<section>.*?<div id="about">.*?</section>)', content, re.DOTALL)
about_part = about_match.group(1)

# Extract footer
footer_match = re.search(r'(<!-- FOOTER -->.*</html>)', content, re.DOTALL)
footer_part = footer_match.group(1)

# Update links function for about-us.html
def make_subpage_links(html):
    html = html.replace('href="#work"', 'href="index.html#work"')
    html = html.replace('href="#process"', 'href="index.html#process"')
    html = html.replace('href="#services"', 'href="index.html#services"')
    html = html.replace('href="#websites"', 'href="index.html#websites"')
    html = html.replace('href="#faq"', 'href="index.html#faq"')
    html = html.replace('href="#hire"', 'href="index.html#hire"')
    
    # Change About link text to About Us
    html = html.replace('href="#about">About<', 'href="about-us.html">About Us<')
    html = html.replace('href="#about" class="mob-link">About<', 'href="about-us.html" class="mob-link">About Us<')
    
    # Change Logo link
    html = html.replace('href="#"', 'href="index.html"')
    
    return html

about_us_html = head_part + '\n' + make_subpage_links(nav_part) + '\n' + make_subpage_links(mob_part) + '\n<main id="main-content" style="padding-top: 100px; min-height: 80vh; display: flex; align-items: center;">\n' + about_part + '\n</main>\n' + footer_part

# Fix the title and canonical URL in about-us.html
about_us_html = about_us_html.replace(
    '<title>YouTube Thumbnail Designer & Shopify Web Developer | Enough Editor</title>', 
    '<title>About Us | Enough Editor</title>'
)
about_us_html = about_us_html.replace(
    '<link rel="canonical" href="https://enougheditorportfolio.vercel.app/">', 
    '<link rel="canonical" href="https://enougheditorportfolio.vercel.app/about-us.html">'
)

with open('about-us.html', 'w', encoding='utf-8') as f:
    f.write(about_us_html)

# Now modify index.html locally
new_index = content

# Replace About links in index.html
new_index = new_index.replace('href="#about">About<', 'href="about-us.html">About Us<')
new_index = new_index.replace('href="#about" class="mob-link">About<', 'href="about-us.html" class="mob-link">About Us<')

# User said "uske andar about us data ho", but didn't explicitly ask to remove it from index.html.
# Usually when splitting to a new page, it is removed from the home page.
# I will remove the about section from index.html.
new_index = new_index.replace(about_part, '')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_index)

print("SUCCESS: about-us.html created and index.html updated locally.")
