import os
from aitextgen import aitextgen

#TODO: support other models such as "minimaxir/hacker-news" or "EleutherAI/gpt-neo-125M" via model parameter
MODEL = os.getenv("MODEL", None)
ai = aitextgen(model=MODEL)
