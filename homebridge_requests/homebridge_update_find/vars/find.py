import globalvars as gv
import helper
from data import *


PARAMS_LIST   = [NAME_LIST]
REQUESTS_LIST = helper.generate_requests(gv.HB['FIND'], PARAMS_LIST, times)
