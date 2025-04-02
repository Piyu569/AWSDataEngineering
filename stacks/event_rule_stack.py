from aws_cdk import (
    Stack,
    aws_events as events,
    aws_events_targets as targets,
    aws_iam as iam
)
from constructs import Construct
from aws_cdk.aws_lambda import Function

class EventRuleStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, lambda_function: Function, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create EventBridge rule
        rule = events.Rule(
            self, "MyEventRule",
            schedule=events.Schedule.rate(cdk.Duration.minutes(5)),  # Runs every 5 minutes
            targets=[targets.LambdaFunction(lambda_function)]
        )

        # Grant EventBridge permission to invoke Lambda
        lambda_function.add_permission(
            "AllowEventBridgeInvoke",
            principal=iam.ServicePrincipal("events.amazonaws.com"),
            action="lambda:InvokeFunction",
            source_arn=rule.rule_arn
        ) 