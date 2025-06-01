from autogen_ext.models.openai import OpenAIChatCompletionClient

def get_model_client():
    """
    Returns the OpenAIChatCompletionClient instance.
    This function is used to ensure that the model client is only created once.
    """
    return OpenAIChatCompletionClient(
        model="gpt-4o-mini",
        temperature=1
    )