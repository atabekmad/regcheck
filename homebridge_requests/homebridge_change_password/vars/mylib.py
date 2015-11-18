

def if_equal_then_save(s1,s2,password):
    if s1.strip() == s2.strip():
        f = open('curr_password','w')
        f.write(password)
        print "Current password " + password + " is saved to curr_password file"
        f.close()


def get_current_password():
    f = open('curr_password','r')
    line = f.readline()
    f.close()
    return line
