import helper 
import globalvars as gv


PARAMS_LIST = [gv.VALID_USERNAME_LIST, gv.PASSWORD, gv.DEVICE_TYPE_LIST]

REQUESTS_LIST = helper.generate_requests(gv.HB["LOGIN"], PARAMS_LIST,2)
