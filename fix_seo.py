import re
import json

file_path = 'c:/Users/abhis/OneDrive/Desktop/ALLPORT/PortfolioSite/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix non-crawlable links
content = content.replace('href="javascript:void(0)" onclick="openModal(\'email\')"', 'href="#contact-email" onclick="openModal(\'email\'); return false;"')
content = content.replace('href="javascript:void(0)" onclick="openModal(\'wa\')"', 'href="#contact-wa" onclick="openModal(\'wa\'); return false;"')
content = content.replace('href="#" class="logo" onclick="window.scrollTo({top: 0, behavior: \'smooth\'}); return false;"', 'href="#top" class="logo" onclick="window.scrollTo({top: 0, behavior: \'smooth\'}); return false;"')
content = content.replace('href="#" class="footer-logo" onclick="window.scrollTo({top: 0, behavior: \'smooth\'}); return false;"', 'href="#top" class="footer-logo" onclick="window.scrollTo({top: 0, behavior: \'smooth\'}); return false;"')

# Enhance JSON-LD Schema
old_schema = '''      {
        "@type": "Person",
        "@id": "https://enougheditorportfolio.vercel.app/#person",
        "name": "Abhishek Rajput",
        "jobTitle": "Lead Designer & Developer",
        "url": "https://enougheditorportfolio.vercel.app/"
      }'''

new_schema = '''      {
        "@type": "Person",
        "@id": "https://enougheditorportfolio.vercel.app/#person",
        "name": "Abhishek Rajput",
        "alternateName": "Enough Editor",
        "jobTitle": "Lead Designer & Developer",
        "url": "https://enougheditorportfolio.vercel.app/",
        "description": "Abhishek Rajput, known professionally as Enough Editor, is a top-tier graphic designer and web developer specializing in high-converting YouTube thumbnails, gaming logos, Shopify stores, and modern digital experiences."
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "Who is Enough Editor?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Enough Editor is the professional moniker of Abhishek Rajput, a lead designer and web developer specializing in YouTube thumbnails, gaming logos, Shopify stores, and modern web applications."
            }
          },
          {
            "@type": "Question",
            "name": "What services does Enough Editor provide?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "Enough Editor provides professional graphic design and web development services, including high-converting YouTube thumbnails, brand identity design, UI/UX design, and custom Shopify store development."
            }
          }
        ]
      }'''

content = content.replace(old_schema, new_schema)

# Write back
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("SEO tags updated")
