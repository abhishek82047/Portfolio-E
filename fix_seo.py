file_path = "c:/Users/abhis/OneDrive/Desktop/ALLPORT/PortfolioSite/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace('href="javascript:void(0)"', 'href="#contactModal"')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Replaced javascript:void(0)")
