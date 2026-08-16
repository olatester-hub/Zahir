# Zahir · Landing page

Landing page estática de **Zahir**, tienda de accesorios femeninos.
Sitio de una sola página, sin dependencias ni proceso de compilación: se publica tal cual.

## Estructura

```
index.html                  la landing completa (HTML + CSS + JS en un archivo)
assets/                     imágenes que se publican en el sitio
  logo-zahir.png            logotipo recortado, fondo transparente
  logo-zahir-oro.png        logotipo monocromo dorado (para el pie oscuro)
  Imagen1..5.jpeg           fotos de producto (5 es de aros)
  video-aros.mp4            video de aros, comprimido con ffmpeg (~580 KB)
  video-aros-poster.jpg     primer fotograma, se muestra mientras carga el video
  video-regalo.mp4          video de empaque/regalo, comprimido con ffmpeg (~430 KB)
  video-regalo-poster.jpg   primer fotograma de ese video
vercel.json                 configuración de Vercel (caché y URLs limpias)
.vercelignore               archivos que quedan en el repo pero no se publican
dist/zahir-landing.html     copia autocontenida (medios incrustados), para compartir por archivo
tools/build_artifact.py     regenera dist/ a partir de index.html
Imagen1..5.jpeg             fotos originales (respaldo, no se publican)
Video1.mp4, Video2.mp4      videos originales sin comprimir (respaldo, no se publican)
LogoMarca.jpeg              logotipo original (respaldo, no se publica)
```

## Ver la página en local

```bash
python3 -m http.server 4321 --directory .
```

Luego abrir http://localhost:4321

## Publicar un cambio

Cada `push` a la rama `main` dispara un despliegue automático en Vercel
(unos 30 segundos hasta que el cambio está en línea).

```bash
git add -A && git commit -m "Actualiza la landing" && git push
```

## Regenerar la copia autocontenida

Solo si cambia `index.html` y quieres actualizar `dist/zahir-landing.html`:

```bash
python3 tools/build_artifact.py
```

Requiere Pillow únicamente si se regeneran los logotipos; para incrustar imágenes basta Python 3.
