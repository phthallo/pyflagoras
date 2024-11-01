from .pyflagoras import Pyflagoras
import json
from importlib.resources import files

flag_aliases_list = "\n".join((json.loads(files("pyflagoras.data").joinpath("flag_aliases.json").read_text(encoding="utf-8"))).keys())
__version__ = "0.5.4"
__list__ = flag_aliases_list
