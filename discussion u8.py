import xml.etree.ElementTree as ET #importing xml reader module
#example 1
files =('Nischal.txt')  #here file name / directory is defined.

try:
    files = open('Nischal.txt')  #if the file name/ directory is matched, then file will open
except:
        print ('Something is wrong, Please try again:', files)  #if the above condition is not fulfilled then the file program crashes but this code handles the case

        
#example 2


name = "namelist.xml"

try:
    read = ET.parse('namelist.xml')

except:
    print ("Could not parse the :", name)

#example 3

   
file_name = "uopeople.docx"
try:
    read_file = open('uopeople.docx')
except:
     print ('No such file or directory found:',file_name)

