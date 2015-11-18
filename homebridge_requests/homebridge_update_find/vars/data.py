import globalvars as gv
import helper


times = 5

NAME_LIST = helper.take_els(gv.VALID_USERNAME_LIST, times)
PASSWORD  = gv.PASSWORD
DATA_LIST = helper.words_list('str_generator(128)', times)
FIRST_NAME = helper.take_els(gv.FIRSTNAME_LIST, times)
LAST_NAME = helper.take_els(gv.LASTNAME_LIST, times)
IP = ' '
EMAIL = gv.EMAIL

used_data = DATA_LIST + FIRST_NAME + LAST_NAME
