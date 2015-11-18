import globalvars as gv
import helper
from data import *


PARAMS_LIST   = [NAME_LIST, PASSWORD, IP, DATA_LIST]
REQUESTS_LIST = helper.generate_requests(gv.HB['UPDATE_DATA'], PARAMS_LIST, times)
