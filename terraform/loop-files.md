# Loop files

Terraform has a `fileset` function that can be used to loop over files in a directory.  
In the below example, we loop over all files in the `website_root` directory and upload them to an S3 bucket.  
(from <https://www.tangramvision.com/blog/abusing-terraform-to-upload-static-websites-to-s3>)

```terraform
resource "aws_s3_bucket_object" "file" {
  for_each = fileset(var.website_root, "**")

  bucket      = aws_s3_bucket.my_static_website.id
  key         = each.key
  source      = "${var.website_root}/${each.key}"
  source_hash = filemd5("${var.website_root}/${each.key}")
  acl         = "public-read"
}
```
