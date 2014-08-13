import math

def main():
    var = int(input("enter number of days: ") )
    if ( var > 0 and var <= 365 ):
       n = math.pow(2, var-1)
       m = n / 100
       print("You earned : $%s"%m)
    else:
         while True:
            print("entered invalid days")
            var = int(input("enter number of days: ") )  
            if ( var > 0 and var <= 365 ):
              n = math.pow(2, var-1)
              m = n / 100
              print("You earned : $%s"%m)
              break
main()         
           
