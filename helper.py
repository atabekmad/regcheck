import string
import random
import connector
import sys
from os.path import dirname
from robot.libraries.BuiltIn import BuiltIn


# Adding root project directory to the PYTHONPATH
sys.path.append(dirname(__file__))

# Getting global variable's value
response = BuiltIn().get_variable_value("${RESPONSE}")


def str_generator(size, chars=string.ascii_letters+string.digits):
    """ Make a random string containing letters and digits """
    return ''.join(random.SystemRandom().choice(chars) for _ in range(size))


def take_els(lst,n):
    return random.sample(lst,n)


def words_list(foo_to_eval, length):
    return [eval(foo_to_eval) for i in range(length)]  


def max_length(lst):
    """ Returns max length of a list inside list """
    list_of_max_length = 0
    for i in range(len(lst)):
        templen = len(lst[i])
        if templen > list_of_max_length:
            list_of_max_length = templen
    return list_of_max_length


def shakelist(lst):
    """ Randomly mixes up a list of elements so that elements don't repeat """
    return random.sample(lst,len(lst))


def equalize(lst, length):
    """ Takes a list of lists and makes length of all lists equal to max_length
        (randomly adds elements to each child list that are < max_length) """
    n_of_lsts = len(lst)
    for n in range(n_of_lsts):
        curr_list = lst[n]
        curr_list_len = len(curr_list)
        if curr_list_len == length:
            pass
        else:
            res = []
            for i in range(length):
                if i >= curr_list_len:
                    res.append(random.choice(curr_list))
                else:
                    res.append(curr_list[i])
            lst[n] = res
    return lst


def single_request(request, params_list):
    return myformat(request, params_list)


def get_params(request):
    """ request  <<< string
        returns  <<< map """
    request = request.replace(" ","")
    request = request[request.find(':')+1:]
    request = request.replace("=,", "=null,")
    request = request.replace(',',' ').replace('=',' ')
    lst = request.split()
    res_dict = {}
    for i in range(len(lst)/2):
        k = i*2
        res_dict[lst[k]] = lst[k+1]
    return res_dict


def myformat(request, *args):
    """ My own format function for creating a formatted string """

    if type(args[0]).__name__ == "list":
        given_args = args[0]
    else:
        given_args = list(args)
    number_of_args = count_request_args(request)
    diff = number_of_args - len(given_args)
    if diff < 0:
        print "Given more args than expected"
        print "Given      : %s" % given_args
        print "In reality : %s" % request
        return
    elif diff > 0:
        for _ in range(diff):
            given_args.append(' ')
    for el in given_args:
        request = request.replace("{}",str(el) ,1)
    return request



def generate_requests(request_template, params_list,  number = 10):
    """  Generates a list of requests (strings) which are sent directly to registry server 
    request_template = request template from globalvars
    params_list = is a list of lists which contain possible variations of request template's params 
    NOTE: Takes 1 request template which is just a string (not a whole dictionary) """

    n_of_params = len(params_list)

    for n in range(n_of_params):
        if type(params_list[n]).__name__ != "list":
            params_list[n] = [params_list[n]]
        params_list[n] = shakelist(params_list[n])

    # length of all arg lists (params_list[i]) will be equal to "number"
    params_list = equalize(params_list, number)

    # Now transform params_list into a list of lists each of which will have enumeration of all arguments
    # For example resulting list looks like this - [[username6,password,ios], [username2,password,android]...]
    res_lst = []
    for col in range( number):
        lst = []
        for row in range(n_of_params):
            lst.append(params_list[row][col])
        res_lst.append(lst)
    params_list = res_lst

    # The actual creation of a list of requests (strings)
    requests = []
    for n in range(number):
        requests.append(myformat(request_template, params_list[n]))

    return requests



def count_request_args(request):
    return request.count('=')


def get_param_names(request):
    param_names = []
    for _ in range(count_request_args(request)):
        pos = request.find('=')
        s = request[:pos]
        s = s[::-1]
        s = s[:s.find(' ')]
        s = s[::-1]
        param_names.append(s)
        request = request[pos+1:]
    return param_names


def generate_invalid_reqs(request_dict, params_dict, number):
    """ Takes requests' dictionary and parameters' dictionary and returns a list of requests (strings) \n
        In parameters' dictionary: \n 
        key = parameter's name          # 'NAME' or 'PASSWORD' or ... \n
        value = parameter's variations  # ['regtest1','regtest4'....] or 'regtest1' or ... \n
        NOTE: Takes a whole dictionary of requests (which btw may have only 1 request), but it must be a dictionary """

    res = []
    for key,req in request_dict.iteritems():
        param_names = get_param_names(req)
        params_list = []
        for i in param_names: 
            params_list.append(params_dict[i])
        res.extend(generate_requests(req,params_list,number))
    return res


# def complete(params=None):



def test(request_template, times=1, *params):
    
#    params = complete(params)
    params = [params]
    requests = generate_requests(request_template,params, times)

    for request in requests:
        conn = connector('shazzledata.com','443')
        conn.send_request(request)
        conn.response_should_be(response)

    print "FINISH"
    
