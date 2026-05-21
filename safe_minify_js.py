import re

js_path = 'c:/Users/abhis/OneDrive/Desktop/ALLPORT/PortfolioSite/js/script.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Safe JS Minification
# Remove single line comments (but not URL protocols like http://)
js = re.sub(r'(?<!:)//.*', '', js)
# Remove block comments
js = re.sub(r'/\*.*?\*/', '', js, flags=re.DOTALL)
# Strip lines and ignore empties
lines = js.split('\n')
out = []
for line in lines:
    l = line.strip()
    if l:
        out.append(l)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))

print("JS safely minified.")
