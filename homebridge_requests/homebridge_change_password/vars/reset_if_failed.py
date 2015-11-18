import globalvars as gv
import data
import mylib



PASSWORD = mylib.get_current_password()
NEWPASSWORD = gv.PASSWORD


REQUEST = gv.HB["CHANGE_PASSWORD"].format(data.USERNAME, PASSWORD, NEWPASSWORD)

