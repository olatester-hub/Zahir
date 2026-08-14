import base64, re, pathlib

base = pathlib.Path(__file__).resolve().parent.parent
html = (base / "index.html").read_text(encoding="utf-8")

# quedarse solo con <title>, <style> y el contenido del <body>
title = re.search(r"<title>.*?</title>", html, re.S).group(0)
style = re.search(r"<style>.*?</style>", html, re.S).group(0)
body = re.search(r"<body>(.*?)</body>", html, re.S).group(1)

doc = f"{title}\n{style}\n{body}"

# incrustar las imágenes como data URIs
def inline(match):
    ruta = match.group(1)
    archivo = base / ruta
    mime = "image/png" if archivo.suffix == ".png" else "image/jpeg"
    datos = base64.b64encode(archivo.read_bytes()).decode()
    return f'src="data:{mime};base64,{datos}"'

doc = re.sub(r'src="(assets/[^"]+)"', inline, doc)

destino = base / "dist" / "zahir-landing.html"
destino.parent.mkdir(exist_ok=True)
destino.write_text(doc, encoding="utf-8")
print(destino, f"{destino.stat().st_size/1_000_000:.2f} MB")
print("quedan rutas relativas:", 'src="assets' in doc)
