from .pyflagoras import Pyflagoras
import json
from importlib.resources import files

flag_aliases_list = "\n".join((json.loads(files("pyflagoras").joinpath("flag_aliases.json").read_text(encoding="utf-8"))).keys())
__version__ = "0.3.3"
__list__ = flag_aliases_list
