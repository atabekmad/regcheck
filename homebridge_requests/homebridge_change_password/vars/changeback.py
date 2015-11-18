import globalvars as gv
import helper
import data
import ok



data.CURRENT_PASSWORD = ok.NEWPASSWORD
NEWPASSWORD = gv.PASSWORD

REQUEST = gv.HB["CHANGE_PASSWORD"].format(data.USERNAME, data.CURRENT_PASSWORD, NEWPASSWORD)

print "Changing password back to " + NEWPASSWORD
