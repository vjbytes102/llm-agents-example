import autogen


def main():
    config_list = {
        "config_list": [
            {
                "model": "lmstudio-community/Phi-3.1-mini-4k-instruct-GGUF",
                "base_url": "http://localhost:1234/v1",
                "api_key": "lm-studio",
            },
        ],
        "cache_seed": None,
        "max_tokens": 1024
    }

    # Create the agent that represents the user in the conversation.
    user_proxy = autogen.UserProxyAgent(
        "user_proxy",
        code_execution_config=False,
        default_auto_reply="...",
        human_input_mode="NEVER"
    )

    # Create the agent that represents the assistant in the conversation.
    sam = autogen.ConversableAgent(
        "sam (Phi-2)",
        llm_config=config_list,
        system_message="""
        Your name is sam and you are a comedian.
        """,
    )

    #initiate conversation
    user_proxy.initiate_chat(sam, message="Tell me a joke!")


if __name__ == "__main__":
    main()