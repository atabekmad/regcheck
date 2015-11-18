import globalvars as gv
import helper
from data import *


PARAMS_LIST   = [NAME_LIST, PASSWORD, FIRST_NAME, LAST_NAME, EMAIL]
REQUESTS_LIST = helper.generate_requests(gv.HB['UPDATE_ACCOUNT'], PARAMS_LIST, times)
