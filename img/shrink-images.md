# Shrink images

Install via `homebrew`:

```bash
brew install pngquant oxipng
```

Reduce image to a maximum of 50 colors:

```bash
pngquant --quality 20-50 image.png
```

Then apply `oxipng`:

```bash
oxipng -o 3 -i 0 --strip safe *-fs8.png
```
