import os
from aitextgen import aitextgen
from protopost import ProtoPost

#TODO: support other models such as "minimaxir/hacker-news" or "EleutherAI/gpt-neo-125M" via model parameter
ai = aitextgen()

PORT = os.getenv("PORT", 80)
DEFAULT_TEMPERATURE = float(os.getenv("DEFAULT_TEMPERATURE", 0.7))
DEFAULT_MAX_LENGTH = int(os.getenv("DEFAULT_MAX_LENGTH", 1024))

def generate(config):
    if type(config) == dict:
        prompt = config["prompt"] if "prompt" in config else ""
        temperature = float(config["temperature"]) if "temperature" in config else DEFAULT_TEMPERATURE
        max_length = int(config["length"]) if "length" in config else DEFAULT_MAX_LENGTH
    else:
        prompt = config if config is not None else ""
        temperature = DEFAULT_TEMPERATURE
        max_length = DEFAULT_MAX_LENGTH

    #TODO: how to get subword length of prompt?
    response = ai.generate_one(prompt=prompt, max_length=len(prompt) + max_length, temperature=temperature)
    response = response[len(prompt):]
    response = response[:max_length]

    return response

routes = {
    "": generate
}

ProtoPost(routes).start(PORT)
