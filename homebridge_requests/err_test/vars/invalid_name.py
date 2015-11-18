import globalvars as gv
import helper
from data import *


REQS = gv.HB


REQUESTS_LIST = helper.generate_invalid_reqs(REQS, invalid_name_params_dict, 2)
