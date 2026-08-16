import base64, re, pathlib

base = pathlib.Path(__file__).resolve().parent.parent
html = (base / "index.html").read_text(encoding="utf-8")

# quedarse solo con <title>, <style> y el contenido del <body>
title = re.search(r"<title>.*?</title>", html, re.S).group(0)
style = re.search(r"<style>.*?</style>", html, re.S).group(0)
body = re.search(r"<body>(.*?)</body>", html, re.S).group(1)

doc = f"{title}\n{style}\n{body}"

# incrustar imágenes y video como data URIs
MIMES = {".png": "image/png", ".jpeg": "image/jpeg", ".jpg": "image/jpeg", ".mp4": "video/mp4"}

def inline(match):
    atributo, ruta = match.group(1), match.group(2)
    archivo = base / ruta
    mime = MIMES[archivo.suffix.lower()]
    datos = base64.b64encode(archivo.read_bytes()).decode()
    return f'{atributo}="data:{mime};base64,{datos}"'

doc = re.sub(r'(src|poster)="(assets/[^"]+)"', inline, doc)

destino = base / "dist" / "zahir-landing.html"
destino.parent.mkdir(exist_ok=True)
destino.write_text(doc, encoding="utf-8")
print(destino, f"{destino.stat().st_size/1_000_000:.2f} MB")
print("quedan rutas relativas:", 'assets/' in doc)
