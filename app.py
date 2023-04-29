#!/usr/bin/env python3
import os

import aws_cdk as cdk
from aws_cdk_deploy.aws_cdk_deploy_stack import AwsCdkDeployStack


app = cdk.App()
AwsCdkDeployStack(
    app,
    "AwsCdkDeployStack",
    env=cdk.Environment(
        account=os.getenv('CDK_DEFAULT_ACCOUNT'),
        region=os.getenv('CDK_DEFAULT_REGION')
        ),
)

app.synth()
