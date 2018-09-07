def  isTCKNumber( tcNo):
    
    if (tcNo is None):
        return false;
        
    #print tcNo[10];
    sum = 0;
    if len(tcNo) == 11:
     for i in range(0,9):
        sum = sum + int(tcNo[i])
        if (sum % 10 == tcNo[10]): 
            return True;
        else:
            return False;



print isTCKNumber("12345678901");
