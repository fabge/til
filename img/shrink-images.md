# Shrink/reduce/compress image sizes

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

The `-o 3` defines level of optimization (`4` is the highest recommended).  
`-i 0` causes it to remove interlacing - "Interlacing can add 25-50% to the size of an optimized image" according to the README.
`--strip safe` strips out any image metadata that is guaranteed not to affect how the image is rendered.
