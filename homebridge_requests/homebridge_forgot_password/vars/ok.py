import helper
import globalvars as gv


PARAMS_LIST = [gv.VALID_USERNAME_LIST]
REQUESTS_LIST = helper.generate_requests(gv.HB['FORGOT_PASSWORD'],PARAMS_LIST,5)
