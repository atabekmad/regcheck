import globalvars as gv
import helper
from data import *


def validate_response(response):

    """ Looks for an intersection between response and used_data (list of all generated data in data.py) """

    resp_values = helper.get_params(response).values()
    matches_num = len(list(set(resp_values).intersection(used_data)))
    print "\nused_data = ", used_data
    print "\nresp_values = ", resp_values

    if matches_num == 3:
        print "\nValidation result - Values do match"
    else:
        msg = "Validation failed. Updated data doesn't correspond to the real data. " + "Matched - " + str(matches_num)
        raise AssertionError(msg)
    
    

