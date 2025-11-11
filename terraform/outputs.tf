output "landing_zone_bucket_name" {
  description = "Name of the S3 landing zone bucket"
  value       = aws_s3_bucket.landing_zone.bucket
}
output "lambda_function_arn" {
  description = "ARN of the ingestion Lambda function"
  value       = aws_lambda_function.ingestion.arn
}

output "dlq_url" {
  description = "URL of the Dead Letter Queue"
  value       = aws_sqs_queue.dlq.id
}

output "scheduler_name" {
  description = "Name of the EventBridge Scheduler"
  value       = aws_scheduler_schedule.ingestion_trigger.name
}

output "s3_bucket_name" {
  description = "Name of the S3 bucket used for ingestion"
  value       = var.bucket_name
}
