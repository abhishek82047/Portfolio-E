import re

file_path = 'c:/Users/abhis/OneDrive/Desktop/ALLPORT/PortfolioSite/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Main tag
content = content.replace('<!-- HERO -->', '<main id="main-content">\n  <!-- HERO -->', 1)
content = content.replace('<!-- FOOTER -->', '</main>\n\n  <!-- FOOTER -->', 1)

# 2. Checkboxes
content = content.replace('class="scroll-checkbox"', 'class="scroll-checkbox" aria-label="Toggle auto scroll"')

# 3. Headings in testimonials
content = re.sub(r'<h4>(.*?)</h4>', r'<h3>\1</h3>', content)

# 4. Footer links
content = content.replace('<a href="https://www.instagram.com/enougheditor?igsh=ZXF5cmZpZmJmMDM3" target="_blank">', '<a href="https://www.instagram.com/enougheditor?igsh=ZXF5cmZpZmJmMDM3" target="_blank" aria-label="Instagram">')
content = content.replace('<a href="https://www.behance.net/enougheditor" target="_blank">', '<a href="https://www.behance.net/enougheditor" target="_blank" aria-label="Behance">')
content = content.replace('<a href="javascript:void(0)" onclick="openModal(\'wa\')"><svg', '<a href="javascript:void(0)" onclick="openModal(\'wa\')" aria-label="WhatsApp"><svg')

# 5. Image dimensions
content = content.replace('id="lbMainImg" src="" alt="Portfolio Image"', 'id="lbMainImg" src="" alt="Portfolio Image" width="1280" height="720"')
content = content.replace('src="assets/Profile Pic/favicon.png" alt="Abhishek Rajput - Enough Editor Logo"', 'src="assets/Profile Pic/favicon.png" alt="Abhishek Rajput - Enough Editor Logo" width="400" height="400"')
content = content.replace('src="assets/Profile Pic/favicon.png" alt="Abhishek Rajput"', 'src="assets/Profile Pic/favicon.png" alt="Abhishek Rajput" width="100" height="100"')
content = content.replace('src="assets/characters/hero_char.webp" alt="3D floating character graphic" class="float-char hero-char reveal" fetchpriority="high"', 'src="assets/characters/hero_char.webp" alt="3D floating character graphic" class="float-char hero-char reveal" fetchpriority="high" width="800" height="800"')
content = content.replace('src="assets/website_pill.webp" alt="Website design portfolio"', 'src="assets/website_pill.webp" alt="Website design portfolio" width="400" height="150"')
content = content.replace('src="assets/shopify_pill.webp" alt="Shopify store design"', 'src="assets/shopify_pill.webp" alt="Shopify store design" width="400" height="150"')
content = content.replace('src="assets/brand_pill.webp" alt="Brand identity design"', 'src="assets/brand_pill.webp" alt="Brand identity design" width="400" height="150"')
content = content.replace('src="./assets/screenshots/ecomtelco.webp?v=1.1" alt="Ecomtelco Website"', 'src="./assets/screenshots/ecomtelco.webp?v=1.1" alt="Ecomtelco Website" width="1280" height="720"')
content = content.replace('src="./assets/screenshots/gmmluxe.webp?v=1.1" alt="GMM Luxe Shopify Store"', 'src="./assets/screenshots/gmmluxe.webp?v=1.1" alt="GMM Luxe Shopify Store" width="1280" height="720"')
content = content.replace('src="./assets/screenshots/perfectcutz.webp?v=1.1" alt="Perfect Cutz Salon Software"', 'src="./assets/screenshots/perfectcutz.webp?v=1.1" alt="Perfect Cutz Salon Software" width="1280" height="720"')
content = content.replace('src="./assets/screenshots/enougheditor_store.webp?v=1.1" alt="Enough Editor Digital Store"', 'src="./assets/screenshots/enougheditor_store.webp?v=1.1" alt="Enough Editor Digital Store" width="1280" height="720"')
content = content.replace('src="assets/characters/hire_char.webp" alt="3D rocket character" class="float-char hire-char reveal delay-2"', 'src="assets/characters/hire_char.webp" alt="3D rocket character" class="float-char hire-char reveal delay-2" width="600" height="600"')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Done fixing HTML issues!')
