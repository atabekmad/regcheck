import globalvars as gv
import helper
import data



NEWPASSWORD = helper.str_generator(48)

REQUEST = gv.HB["CHANGE_PASSWORD"].format(data.USERNAME, data.CURRENT_PASSWORD, NEWPASSWORD)

print "Changing password to " + NEWPASSWORD



