from strands import Agent
from strands.models import BedrockModel
from strands_tools import calculator

provisioned_model = BedrockModel(
    model_id="arn:aws:sagemaker:ap-southeast-1:412254469544:endpoint/endpoint-quick-start-tb5e6",
    streaming=False
)

agent = Agent(
    model=provisioned_model,
    system_prompt="You are a specialist using Marketplace models via Strands.",
 #   tools=[calculator]
)

# 3. Execute
response = agent("What is 15% of 1240?")
print(response.message)