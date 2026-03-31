from datetime import datetime    
def is_valid(date):   #function that takes a date as input parameter.   
        try:           
           if len((str(datetime.strptime(date,"%m-%d-%Y")))==10 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(date[:2]) > 31):   #checking for number of days in the month
                return False 
           if len((str(datetime.strptime(date,"%m-%d-%Y")))==8 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(date[:1]) > 30):   #checking for number of days in the month
                return False 
           if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(date[:1]) > 30):   #checking for number of days in the month
                return False           
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==7 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(date[:1]) > 30):   #checking for number of days in the month
                return False 
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(date[:4]) -10 )>35 ):   #checking for number of days in the year
                return False         
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(date[:4]) -10 )>35 ):   #checking for number of days in the year
                return False         
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float(date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year   
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float(date[:4])+10 ) - 35   )>67:   
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==8 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float(date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year   
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking for number of days in the year    
            if len((str(datetime.strptime(date,"%m-%d-%Y")))==9 and (len(re.findall('[aA]n', str(datetime)))!=2 or int(int(float( date[:4])+10 ) - 35   )>67:
                return False          #checking