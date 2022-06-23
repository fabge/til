# ERR_TOO_MANY_REDIRECTS

I tried setting up a static site with [S3 and Cloudfront](../aws/s3-cloudfront-pretty-urls.md) and managing the domain with [Cloudflare](https://www.cloudflare.com/).
Even when S3, Cloudfront and Cloudflare were set up correctly, requests to the newly setup website returned a very nondescript error:

![err_too_many_redirects](err_too_many_redirects.png)

After some googling, the solution turned out to be to set the Cloudflare SSL/TLS encryption mode to `Full` instead of the default `Flexible`.
