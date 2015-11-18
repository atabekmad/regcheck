import globalvars
import helper
from data import *


PARAMS_LIST = [NAME_LIST, PASSWORD]
REQUESTS_LIST = helper.generate_requests(gv.HB['DELETE'], PARAMS_LIST, TIMES)
