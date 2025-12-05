"""
Agent configuration module for Strands agent initialization.
"""
import os
from strands import Agent
from strands.models.openai import OpenAIModel
from strands_tools import calculator, current_time
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

# Default model configuration
MODEL_CONFIG = {
    "model_id": "gpt-4o",
    "params": {
        "max_tokens": 1000,
        "temperature": 0.7,
    }
}

# Default tools that will be included in every agent
DEFAULT_TOOLS = [calculator, current_time]

def myAgent(additional_tools=None):
    """
    Create a pre-configured Strands agent with OpenAI model.
    
    Args:
        additional_tools (list, optional): Additional tools to add beyond defaults
    
    Returns:
        Agent: Configured Strands agent ready to use
    """
    # Create the model
    model = OpenAIModel(
        client_args={"api_key": API_KEY},
        model_id=MODEL_CONFIG["model_id"],
        params=MODEL_CONFIG["params"]
    )
    
    # Combine default tools with any additional tools
    tools = DEFAULT_TOOLS.copy()
    if additional_tools:
        if not isinstance(additional_tools, list):
            additional_tools = [additional_tools]
        tools.extend(additional_tools)
    
    return Agent(model=model, tools=tools)