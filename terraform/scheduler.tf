resource "aws_iam_role" "scheduler_role" {
  name = "eventbridge-scheduler-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect = "Allow",
      Principal = {
        Service = "scheduler.amazonaws.com"
      },
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy" "scheduler_policy" {
  name = "eventbridge-scheduler-policy"
  role = aws_iam_role.scheduler_role.id

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect = "Allow",
      Action = "lambda:InvokeFunction",
      Resource = aws_lambda_function.ingestion.arn
    }]
  })
}

resource "aws_scheduler_schedule" "ingestion_trigger" {
  name       = "open-meteo-ingestion-schedule"
  group_name = "default"

  schedule_expression = "rate(1 hour)"

  flexible_time_window {
    mode = "OFF"
  }

  target {
    arn      = aws_lambda_function.ingestion.arn
    role_arn = aws_iam_role.scheduler_role.arn
  }
}
