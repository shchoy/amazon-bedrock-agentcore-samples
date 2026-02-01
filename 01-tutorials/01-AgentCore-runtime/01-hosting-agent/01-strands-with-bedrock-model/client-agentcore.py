import boto3
import json
import uuid

client = boto3.client('bedrock-agentcore', region_name='ap-southeast-1')
payload = json.dumps({"prompt": "Explain machine learning in simple terms"})

response = client.invoke_agent_runtime(
    agentRuntimeArn='arn:aws:bedrock-agentcore:ap-southeast-1:412254469544:runtime/agent_01-96YBhQAIea',
    runtimeSessionId=str(uuid.uuid4()), # Must be 33+ char. Every new SessionId will create a new MicroVM
    payload=payload,
    qualifier="DEFAULT" # This is Optional. When the field is not provided, Runtime will use DEFAULT endpoint
)
response_body = response['response'].read()
response_data = json.loads(response_body)
print("Agent Response:", response_data)