import subprocess
import os
logfile ="/var/log/syslog"
out=subprocess.check_output("ls -s "+logfile,shell=True)

print out
a=out.split( )

print a[0]



if int(a[0]) > 10000 :
    print logfile+ " >10000"
    os.system("sudo truncate -s0 "+logfile)

#-----------------------------------------------------------
#logfile ="/var/log/upstart/SUT-moisture.log"
#out=subprocess.check_output("ls -s "+logfile,shell=True)

#print out
#a=out.split( )

#print a[0]



#if int(a[0]) > 10000 :
#    print logfile+ " >10000"
#    os.system("sudo truncate -s0 "+logfile)


logfile ="/var/log/messages"
out=subprocess.check_output("ls -s "+logfile,shell=True)

print out
a=out.split( )

print a[0]

if int(a[0]) > 10000 :
    print logfile+ " >10000"
    os.system("sudo truncate -s0 "+logfile)

	
logfile ="/var/log/daemon.log"
out=subprocess.check_output("ls -s "+logfile,shell=True)

print out
a=out.split( )

print a[0]

if int(a[0]) > 10000 :
    print logfile+ " >10000"
    os.system("sudo truncate -s0 "+logfile)    
    	

logfile ="/var/log/auth.log"
out=subprocess.check_output("ls -s "+logfile,shell=True)

print out
a=out.split( )

print a[0]

if int(a[0]) > 10000 :
    print logfile+ " >10000"
    os.system("sudo truncate -s0 "+logfile)    

	
	

logfile ="/var/log/kern.log"
out=subprocess.check_output("ls -s "+logfile,shell=True)

print out
a=out.split( )

print a[0]

if int(a[0]) > 10000 :
    print logfile+ " >10000"
    os.system("sudo truncate -s0 "+logfile)    
    
