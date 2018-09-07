def isVKNumber(vkn):
  sum = 0
  j = 9
  for i in range(0,8):
    #print "vkn[i]",vkn[i],i;
    i1 = (int(vkn[i])+ 10-(i+1))% 10;
    #print "i1 :",i1;
    i2 = (i1 * (2 ** j)) % 9;
    #print "i2 :",i2;
    if (i1!=0 and i2==0):
        sum =sum+9;
    else:
        sum=sum+i2;
    j = j - 1;
  
  #print "toplam :",sum;
 
  if (sum % 10 == 0) :        
    lastdigit = 0;
  else:
    lastdigit =   (10 - (sum % 10));
  #print "lastdigit :",lastdigit;
  
  if (lastdigit == int(vkn[len(vkn)-1])):
	return  True;
  else:
    return False;

print isVKNumber("4610377893");