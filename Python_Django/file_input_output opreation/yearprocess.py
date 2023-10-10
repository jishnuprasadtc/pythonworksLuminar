  
#read from year.txt
fr=open("C:\\Users\\DELL\\OneDrive\\Desktop\\Python_Django\\file_input_output opreation\\year.txt")
lw=open("C:\\Users\\DELL\\OneDrive\\Desktop\\Python_Django\\file_input_output opreation\\leaper.txt","w")
lw=open("C:\\Users\\DELL\\OneDrive\\Desktop\\Python_Django\\file_input_output opreation\\notleaper.txt","w")

for y in range(1800,2025):
    fr.read(y)
    print(y)

# write leapyear in to leaper txt
leaper=[leap for leap in range(1800,2050) 
         if((leap % 400 == 0) or 
             (leap % 100 != 0) and 
               (leap % 4 == 0))]
lw.write(str(leaper)+"\n")

 # write non leaper year to non leaper txt
notleapear=[nonleaps  for nonleaps in range(1800,2025)  
            if((nonleaps% 400 != 0) or 
             (nonleaps % 100 != 0) and 
               (nonleaps % 4 != 0)) ]
lw.write(str(notleapear))




#**************************************************************************************************************************





