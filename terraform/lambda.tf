resource "aws_iam_role" "lambda_ingestion_role" {
  name = "lambda-ingestion-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect = "Allow",
      Principal = {
        Service = "lambda.amazonaws.com"
      },
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy" "lambda_ingestion_policy" {
  name = "lambda-ingestion-policy"
  role = aws_iam_role.lambda_ingestion_role.id

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Action = [
          "s3:PutObject",
          "s3:GetObject",
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents",
          "cloudwatch:PutMetricData",
          "sqs:SendMessage"
        ],
        Resource = "*"
      }
    ]
  })
}

resource "aws_lambda_function" "ingestion" {
  function_name = "open-meteo-ingestion"
  role          = aws_iam_role.lambda_ingestion_role.arn
  handler       = "main.lambda_handler"
  runtime       = "python3.11"
  timeout       = 30

  filename         = "${path.module}/../lambda_ingestion/lambda.zip"
  source_code_hash = filebase64sha256("${path.module}/../lambda_ingestion/lambda.zip")

  dead_letter_config {
    target_arn = aws_sqs_queue.dlq.arn
  }

  environment {
    variables = {
      BUCKET_NAME = "my-data-pipeline-landing-zone"
    }
  }
}
