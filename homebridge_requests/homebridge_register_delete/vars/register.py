import globalvars
import helper
from data import *


DOMAIN = ' '
TOKEN  = ''


PARAMS_LIST = [NAME_LIST, PASSWORD, DOMAIN, EMAIL, TOKEN]
REQUESTS_LIST = helper.generate_requests(gv.HB['REGISTER'], PARAMS_LIST, TIMES)
