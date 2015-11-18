import helper
from data import *


PARAMS_LIST = [NAME_LIST, PASSWORD, 'unknown']
REQUESTS_LIST = helper.generate_requests(gv.HB["LOGIN"], PARAMS_LIST, TIMES)

