import os
from aitextgen import aitextgen

MODEL = os.getenv("MODEL", None)
ai = aitextgen(model=MODEL)
