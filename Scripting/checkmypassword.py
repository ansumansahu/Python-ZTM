from operator import ge
import sys
import requests
import hashlib

def request_api_data(query_char):
    url='http://api.pwnedpasswords.com/range/'+query_char
    res= requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error Fetching : {res.status_code}, check api again')
    return res

def get_password_leaks_count(hashes, hash_to_check): #has_to_check is rest_char of our password in hashed form
    #hashes is all the response api grabs from first 5 char of our hash
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h,count in hashes:
        if h==hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    #check password if it exits in API response
    sha1password=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5char,rest_char=sha1password[:5],sha1password[5:]
    response = request_api_data(first_5char)
    return get_password_leaks_count(response, rest_char) 

def main(args):
    for password in args:
        count=pwned_api_check(password)
        if count:
            print(f'The password was found {count} times. Consider changing it buddy')
        else:
            print(f'Woah now that\'s a secure password. Way to go Buddy')
    return 'Done!!'

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))

'''
The website takes the first 5 digit of the 'SHA 1 hash'
so we actually generate a SHA 1 hash of our password and then just pass the first five digits of the hash
so we are keeping safe our hash, so that no one can even backtrace the password using our hash.
and this website list all the hash starting with the 5 digits we have passed, and we can then manually check whether our 
password has been hacked or not
'''