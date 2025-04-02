#!/usr/bin/env python3
import aws_cdk as cdk
from stacks.lambda_stack import LambdaStack
from stacks.event_rule_stack import EventRuleStack

app = cdk.App()

# Create the Lambda stack
lambda_stack = LambdaStack(app, "LambdaStack")

# Create the Event Rule stack and pass the Lambda function
event_rule_stack = EventRuleStack(app, "EventRuleStack", 
                                lambda_function=lambda_stack.lambda_function)

app.synth() 