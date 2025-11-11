output "landing_zone_bucket_name" {
  description = "Name of the S3 landing zone bucket"
  value       = aws_s3_bucket.landing_zone.bucket
}
