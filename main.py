
from config import myAgent
from tools import *

agent = myAgent()
agent = myAgent(additional_tools=[letter_counter])

message = """
I have 4 requests:

1. What is the time right now?
2. Calculate 3111696 / 74088
3. Tell me how many letter R's are in the word "strawberry" 🍓
"""

response = agent(message)
print(response)