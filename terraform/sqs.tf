resource "aws_sqs_queue" "dlq" {
  name                      = "open-meteo-dlq"
  message_retention_seconds = 1209600  # 14 days
  visibility_timeout_seconds = 30
}