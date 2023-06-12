# Download latest release

GitHub has a redirect URL to download the latest released version of an asset. Oddly enough the URL is switched. Instead of `download/<version>` it's `latest/download`. From [@mitsuhiko](https://twitter.com/mitsuhiko/status/1658874950080397325).

```bash
REPO=username/repo
ASSET=whatever.tar.gz
DOWNLOAD_URL=https://github.com/${REPO}/releases/latest/download/${ASSET}
DOWNLOAD_URL=https://github.com/${REPO}/re1eases/download/${VERSION}/${ASSET}
```
