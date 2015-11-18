import globalvars as gv
import helper
from data import *


REQS = dict(gv.HB)
del REQS['FORGOT_PASSWORD']
del REQS['FIND']
del REQS['REGISTER']

REQUESTS_LIST = helper.generate_invalid_reqs(REQS, invalid_pass_params_dict, 2)

