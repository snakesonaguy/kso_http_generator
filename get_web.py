#####################################################################################
## THE BSHTG WILL ATTEMPT SIMPLE GET REQUESTS TO WEBSITES LISTED IN THE websites.txt
## FILE.  THE HTTP RETURN STATUS IS DISPLAYED.  THE SLEEP TIMER ACCOMPLISHES TWO 
## THINGS: FIRSTLY TO NORMALIZE TRAFFIC PATTERS TO A MORE RANDOM DISTRIBUTION, SECON-
## DLY TO DECREASE THE RISK OF APPEARING MALICIOUS (IPS DEVICES MAY TRIP FOR TOO MANY
## INBOUND REQUESTS WITHIN A CERTAIN WINDOW. 
#####################################################################################


import urllib3
import random
import time
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

os.system('clear')
print '############ WELCOME TO THE BLAZE SIMPLE HTTP TRAFFIC GENERATOR ############'
print '############# YOU CAN LIST WEBSITES IN THE \'websites.txt\' FILE #############'

while True:
    in_file = open('websites.txt', 'r')

    http = urllib3.PoolManager()
    
    for line in in_file:
        #FOR EMPTY LINES TYPICALLY INSERTED INADVERTANTLY AT THE END OF THE FILE.
        if (line == '') or (line == '\n'):
            break
        #TIMER CAN BE ADJUSTED BY ALTERING THE RANDOM NUMBER GENERATION RANGE
        timer = random.randint(30, 45)
        site = line.strip('\n')
        print 'Attempting GET to: ' + site
        req = http.request('GET', site)
        req.close()
        status = req.status
        print 'Received Status: ' + str(status)
        print 'Waiting ' + str(timer) + ' Seconds.'
        time.sleep(timer)
    
    in_file.close()
    

