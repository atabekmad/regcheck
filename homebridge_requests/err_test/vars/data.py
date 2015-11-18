import helper
import globalvars as gv


# valid parameters
VALID_NAME = gv.VALID_USERNAME_LIST
VALID_PASS = gv.PASSWORD
DEVICE_TYPE = gv.DEVICE_TYPE_LIST
FIRSTNAME = gv.FIRSTNAME_LIST
LASTNAME = gv.LASTNAME_LIST
EMAIL = 'atabek@shazzle.com'
DATA = ' '
TOKEN = ''
IP = '127.0.0.1'
DOMAIN = ' '
VERSION = gv.VERSION


# invalid parameters
INVALID_NAME = [' ', '%$#@^($', 'sad|xz||',]
INVALID_PASS = helper.words_list("str_generator(64)",3)


valid_params_dict = {
    'NAME':VALID_NAME,
    'PASSWORD': VALID_PASS,
    'DEVICE_TYPE':DEVICE_TYPE,
    'DOMAIN': DOMAIN,
    'EMAIL': EMAIL,
    'FIRST_NAME': FIRSTNAME,
    'LAST_NAME' : LASTNAME,
    'IP': IP,
    'TOKEN': TOKEN,
    'NEWPASSWORD' : VALID_PASS,
    'DATA': DATA,
    'VERSION': VERSION,
}


invalid_name_params_dict = dict(valid_params_dict)
invalid_pass_params_dict = dict(valid_params_dict)
empty_name_params_dict   = dict(valid_params_dict)
empty_pass_params_dict   = dict(valid_params_dict)


invalid_pass_params_dict['PASSWORD'] = INVALID_PASS
invalid_name_params_dict['NAME']     = INVALID_NAME
empty_name_params_dict['NAME']       = ''
empty_pass_params_dict['PASSWORD']   = ''





