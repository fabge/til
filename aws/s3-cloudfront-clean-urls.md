# S3 + Cloudfront + clean URLs

From [Building a static serverless website using S3 and CloudFront](https://sanderknape.com/2020/02/building-a-static-serverless-website-using-s3-cloudfront/):
> The common advice then is to use Amazon CloudFront as a CDN in front of S3. CloudFront supports HTTPS - including for custom domains - and has built-in support for S3 using an [Origin Access Identity](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) (OAI). The OAI is used to authenticate CloudFront to S3 and ensure that the content is only available through the CloudFront endpoint. However, CloudFront uses the REST endpoint when connecting to S3 through the OAI instead of the website endpoint. This is severely limiting as the REST endpoint does not support redirecting requests to an index object. For example, when visiting `example.com/about/`, you will typically want to serve the file `example.com/about/index.html` to the visitor. This is supported with the website endpoint, but not with the REST endpoint that CloudFront uses when connecting it through the OAI.

The solution:
> We configure CloudFront to forward an additional Referer header to the origin endpoint (our S3 website endpoint) as it connects to it. This header is completely invisible to the visitor accessing the website.