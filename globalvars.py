PASSWORD = 'W6ph5Mm5Pz8GgiULbPgzG37mj9g_'
EMAIL    = 'atabek@shazzle.com'
VERSION  = 2



# PARAMS = {
#     "NAME"        :   {
#         "VALID"      : [['regtest','regtest1','regtest2','regtest3','regtest4','regtest5','regtest6','regtest7','regtest8','regtest9']
#                      ['atabekdesktop','atabek','ahb','ahbdot','ahbdot1']],
#         "INVALID"    : [[' ', '%$#@^($', 'sad|xz||',]]
#         },
#     "PASSWORD"    :   {
#         "VALID"


# PARAMS.get(name,valid,

    

VALID_USERNAME_LIST      = ['regtest','regtest1','regtest2','regtest3','regtest4','regtest5','regtest6','regtest7','regtest8','regtest9']
DEVICE_TYPE_LIST         = ['ios','android']
FIRSTNAME_LIST           = ['Atabek', 'Ruslan', 'Vadim', 'Yura', 'Navruz', 'Murod', 'Aleksey', 'Kseniya', 'Susha', 'Evgeniy', 'Jawid', 'Petro', 'Vladimir']
LASTNAME_LIST            = ['Madaminov', 'Salikhov', 'Topchiy', 'Yugay', 'Akhmedov', 'Almatov', 'Mironenko', 'Habibi', 'Verheles', 'Shin', 'Lisenko']
NOTCREATED_USERLIST      = ["regtest"+str(x) for x in range(10,100)]  
VALID_USERPASS_DICT      = {key : PASSWORD for key in VALID_USERNAME_LIST}


HB = {
    "LOGIN"                : "HOMEBRIDGE_LOGIN:              NAME={}, PASSWORD={}, DEVICE_TYPE={}",
    "REGISTER"             : "HOMEBRIDGE_REGISTER:           NAME={}, PASSWORD={}, DOMAIN={}, EMAIL={}, TOKEN={}",
    "CHANGE_PASSWORD"      : "HOMEBRIDGE_CHANGE_PASSWORD:    NAME={}, PASSWORD={}, NEWPASSWORD={}",
    "UPDATE_DATA"          : "HOMEBRIDGE_UPDATE_DATA:        NAME={}, PASSWORD={}, IP={}, DATA={}",
    "UPDATE_ACCOUNT"       : "HOMEBRIDGE_UPDATE_ACCOUNT:     NAME={}, PASSWORD={}, FIRST_NAME={}, LAST_NAME={}, EMAIL={}",
    "REQUEST_RELAY_LIST"   : "HOMEBRIDGE_REQUEST_RELAY_LIST: NAME={}, PASSWORD={}, VERSION={}",
    "DELETE"               : "HOMEBRIDGE_DELETE:             NAME={}, PASSWORD={}",
    "FORGOT_PASSWORD"      : "HOMEBRIDGE_FORGOT_PASSWORD:    NAME={}",
    "FIND"                 : "HOMEBRIDGE_FIND:               NAME={}",
}


# Response code
OK                 = "OK"
FAILED             = "FAILED"
FAILED_NOT_EXISTS  = "FAILED_NOT_EXISTS"




# PARAMS = {
#     "NAME" : {
#         'VALID'    : ['regtest', 'regtest1', 'regtest2', 'regtest3', 'regtest4', 'regtest5', 'regtest6', 'regtest7', 'regtest8', 'regtest9'],
#         'INVALID'  : NOTCREATED_USERLIST,
#     },
#     "PASSWORD"     : 'W6ph5Mm5Pz8GgiULbPgzG37mj9g_',
#     "DEVICE_TYPE"  : ['ios','android'],
#     'FIRST_NAME'   : FIRSTNAME_LIST,
#     'LAST_NAME'    : LASTNAME_LIST,
#     'EMAIL'        : EMAIL,
#     'DATA'


# PARAMS["NAME"]["VALID"][0]

