
#Calculating user's salary according to the number of days given by user and capturing the output in a file


#PsuedoCode
#Step 1 : User Input from stdin, Enter number of days
#step 2 : Take the days as argument to the condition
#step 3 : Check the condition if the number of days are valid i.e. 1 to 366 inclusive
#step 4 : If the condition is true calculate the result using 2^n-1
#step 5 : Convert cents to dollar using divide by 100 from the result obtained from step 4
#step 6 : If the condition is false display a message saying you have entered invalid days
#step 7 : Ask the user to re-enter valid number of days
#step 8 : Check the condition , if it is true execute the result like in step #4
#step 9 : If it is false , ask the user to re-enter the valid number of days again and continue
#step 10 : Once the condition is true break the loop and display the result
#step 11 : Stop



#Programming
import math    #math calculation
import time

def main():
    filename = time.strftime('%A-%Y%m%d-%H-%M-%S') + '.txt'  # filename with system date time format
    f = open(filename , 'w') # opening the file with write 'w' permission
    
    f.write('+++++++++++++++++++++++++++++++++\n') # decoration with +++
    print('+++++++++++++++++++++++++++++++++')
            #To add the characters/decorating output
    days = int(input("Please enter number of days: ") )   #Asking user input
    f.write('days:  %s'%days)                             # Writing the user input 'days' to the text file
    if ( days > 0 and days <= 366 ):                      #condition to check valid days in a year
        n = math.pow(2, days-1)                           #power function ...2^n-1
        m = n / 100                                       #Converting cents to dollars
        f.write('\n+++++++++++++++++++++++++++++++++\n')
        print('+++++++++++++++++++++++++++++++++')
        f.write(' Day   Today\'s Salary \n------  -----------------\n %s    $%s'%(days,m))   #%s-substitution %(days,m) using variable to display output
        print(' Day   Today\'s Salary \n------  -----------------\n %s    $%s'%(days,m))    #%s-substitution %(days,m) using variable to display output 
    else:
        while True:                                                    #looping to check whether user has entered valid data
            f.write("\nInvalid number of days\n")               # Writing invalid number of days to text file
            print("Invalid number of days\n")
            f.write('+++++++++++++++++++++++++++++++++\n')      # decoration with +++ in the text file
            print('+++++++++++++++++++++++++++++++++\n')
            days = int(input("Please enter number of days: ") ) #Asking user input
            f.write('days:  %s'%days)
            #print ('------------------------------')  
            if ( days > 0 and days <= 366 ):
                n = int(math.pow(2, days-1))
                m = n / 100
                print ('+++++++++++++++++++++++++++++++++\n')
                f.write('\n+++++++++++++++++++++++++++++++++\n')
                f.write(' Day   Today\'s Salary\n------  -------------------\n %s    $%s'%(days,m))
                print(' Day   Today\'s Salary\n------  -------------------\n %s    $%s'%(days,m))
                break                                                      #breaking the loop
    
    

main()          #calling main function

