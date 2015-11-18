import helper
import globalvars as gv


PARAMS_LIST = [gv.VALID_USERNAME_LIST, gv.PASSWORD, gv.VERSION]
REQUESTS_LIST = helper.generate_requests(gv.HB['REQUEST_RELAY_LIST'], PARAMS_LIST, 5)
