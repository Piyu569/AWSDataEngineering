# AWS Lambda with EventBridge Integration

This project demonstrates the integration of AWS Lambda with EventBridge (CloudWatch Events) using AWS CDK.

## Project Structure

```
.
├── app.py                 # Main CDK app
├── requirements.txt       # Python dependencies
├── stacks/               # CDK stack definitions
│   ├── lambda_stack.py   # Lambda function stack
│   └── event_rule_stack.py # EventBridge rule stack
├── lambda/               # Lambda function code
│   └── index.py         # Lambda handler
└── .github/             # GitHub Actions workflows
    └── workflows/
        └── cdk.yml      # CDK deployment workflow
```

## Prerequisites

- AWS CLI configured with appropriate credentials
- Python 3.9 or later
- AWS CDK CLI installed (`npm install -g aws-cdk`)

## Setup

1. Create a virtual environment and activate it:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Bootstrap CDK (first time only):
```bash
cdk bootstrap
```

## Deployment

### Local Deployment

```bash
cdk deploy --all
```

### GitHub Actions Deployment

1. Add the following secrets to your GitHub repository:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`

2. Push to the main branch to trigger the deployment workflow.

## Features

- Lambda function that logs execution time
- EventBridge rule that triggers the Lambda every 5 minutes
- IAM roles and permissions automatically configured
- Automated deployment through GitHub Actions

## Customization

- Modify the Lambda function code in `lambda/index.py`
- Adjust the EventBridge schedule in `stacks/event_rule_stack.py`
- Update the AWS region in `.github/workflows/cdk.yml`