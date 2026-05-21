import re

html_path = 'c:/Users/abhis/OneDrive/Desktop/ALLPORT/PortfolioSite/index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Add loading="lazy" to all <img in .p-card if not already there
html = re.sub(r'(<img)(.*?src="assets/(Thumbnail|Gaming Logo|Short Thumbnails)[^>]+>)', 
              lambda m: m.group(0) if 'loading=' in m.group(0) else m.group(1) + ' loading="lazy"' + m.group(2), 
              html)

# Also ensure width and height for these images if not present. Wait, they already have width/height from the output earlier, let me check:
# index.html:289:          <div class="p-card"><img  decoding="async" width="1280" height="720" src="assets/Thumbnail/Bgmi Gaming thumbnail.jpg"
# It seems they DO have width/height. I just need to add loading="lazy".

html = html.replace('href="css/style.css"', 'href="css/style.min.css"')
html = html.replace('src="js/script.js"', 'src="js/script.min.js"')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML updated")

css_path = 'c:/Users/abhis/OneDrive/Desktop/ALLPORT/PortfolioSite/css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Simple CSS minifier
css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL) # remove comments
css = re.sub(r'\s+', ' ', css) # reduce whitespace
css = re.sub(r'\s*([\{\}\:\;\,\>\+\~\(\)])\s*', r'\1', css) # remove spaces around syntax
css = css.replace(';}', '}')

with open('c:/Users/abhis/OneDrive/Desktop/ALLPORT/PortfolioSite/css/style.min.css', 'w', encoding='utf-8') as f:
    f.write(css.strip())
print("CSS minified")

js_path = 'c:/Users/abhis/OneDrive/Desktop/ALLPORT/PortfolioSite/js/script.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Simple JS minifier (basic whitespace removal)
js = re.sub(r'//.*', '', js) # single line comments
js = re.sub(r'/\*.*?\*/', '', js, flags=re.DOTALL) # multi line
# We can't aggressively remove whitespace in JS without a proper AST, but we can do safe ones
lines = js.split('\n')
out = []
for line in lines:
    l = line.strip()
    if l:
        out.append(l)

with open('c:/Users/abhis/OneDrive/Desktop/ALLPORT/PortfolioSite/js/script.min.js', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
print("JS minified")

