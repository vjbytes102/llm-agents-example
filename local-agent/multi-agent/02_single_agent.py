
import autogen

configuration_list = [
    {
      "model": "mistral",
      "api_key": "lm-studio",
      "base_url": "http://localhost:1234/v1"
    }
]

# Create the agent that represents the user in the conversation.
user_agent = autogen.UserProxyAgent(
    "client",
    code_execution_config={
        "work_dir": "coding_01",
        "use_docker": False
    },
    human_input_mode="NEVER",
    is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
    default_auto_reply="Reply 'TERMINATE' in the end when everything is done. ",
    max_consecutive_auto_reply=5
)

# Create the agent that represents the assistant in the conversation.
developer = autogen.AssistantAgent(
    "developer",
    llm_config={"config_list": configuration_list},
    system_message="You are a 10x Python Engineer.  You only code in Python.  You create excellent front-end "
                "developer. Make sure to have # filename: <name of the file>.py as the first line after the triple tick marks. "
                "When you are done, reply with TERMINATE.",
)

user_agent.initiate_chat(
    developer,
    message="I want you to create two different python methods for me in 1 file.  1 will just generate a random number, and the other will take in a number and then reverse it."
)