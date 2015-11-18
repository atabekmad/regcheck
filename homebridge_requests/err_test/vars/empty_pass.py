import globalvars as gv
import helper
from data import *


REQS = dict(gv.HB)
del REQS['FORGOT_PASSWORD']
del REQS['FIND']

REQUESTS_LIST = helper.generate_invalid_reqs(REQS, empty_pass_params_dict, 2)


