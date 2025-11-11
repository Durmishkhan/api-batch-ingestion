resource "aws_s3_bucket" "landing_zone" {
  bucket        = var.bucket_name
  force_destroy = true

  tags = {
    Name        = "LandingZone"
    Environment = var.environment
    Project     = "ServerlessBatchIngestion"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "default_encryption" {
  bucket = aws_s3_bucket.landing_zone.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_lifecycle_configuration" "raw_data_lifecycle" {
  bucket = "my-data-pipeline-landing-zone" 

  rule {
    id     = "raw-data-expiration"
    status = "Enabled"

    filter {
      prefix = "raw/"
    }

    transition {
      days          = 15
      storage_class = "GLACIER"
    }

    expiration {
      days = 30
    }
  }
}
