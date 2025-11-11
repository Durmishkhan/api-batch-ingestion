import boto3

cloudwatch = boto3.client("cloudwatch")

def emit_metric(count):
    
    cloudwatch.put_metric_data(
        Namespace="IngestionPipeline",
        MetricData=[{
            "MetricName": "records_processed",  
            "Value": count,                    
            "Unit": "Count"                     
        }]
    )
