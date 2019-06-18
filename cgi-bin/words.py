#!/usr/bin/python3
# Import modules for CGI handling 
import cgi, cgitb 
import re
import document_analyser as d_analyse
# Create instance of FieldStorage 
form = cgi.FieldStorage() 
#-------------------------- REGULAR EXPRESSION FOR URL VALIDATION -----------------------------------
regex = re.compile(

        r'^(?:http|ftp)s?://' # http:// or https://

        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...

        r'localhost|' #localhost...

        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip

        r'(?::\d+)?' # optional port

        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

# Get data from fields
URL = form.getvalue('input_file1')
filePath  = form.getvalue('input_file2')

def analyse_input(URL,filePath):
    
    if URL and filePath:
        print("<h3> ERROR: You have Entered Values in both the fields</h3>")
    elif URL:
       # call a utility functioon to check url correctness
        if(re.match(regex,URL)):
            
            f_text_data = d_analyse.get_file_data(URL)
            #call the utility functioon to analyse the text
            max_dict, min_dict, word_count = d_analyse.parse_into_dict(f_text_data)
            

            return max_dict, min_dict, word_count,"URL"
        else:
            print("<h3> ERROR: Enter Correct Path</h3>")
            

    elif filePath:
        text_data = d_analyse.analyse_text(filePath)
        #call the utility functioon to analyse the text
        max_dict, min_dict, word_count = d_analyse.parse_into_dict(text_data)
        return max_dict, min_dict, word_count,"Text"

    else:
        #please enter the values in required fields
        print("<h3> ERROR: Please Enter a File Url or Text to be Analysed")
         

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Word Analyser</title>")
print ("</head>")
print ("<body>")
max_dict, min_dict, word_count,typeOfInput = analyse_input(URL,filePath)
if(typeOfInput=="URL"):
    print("<h3> Word Count Statistics for %s:</h3>"%(URL)) 
else:
    print("<h3> Word Count Statistics for text provided on input</h3>")
print("<p> The document contains %s words"%(str(word_count)))

print("<table border='0' >")
print("<tbody>")
print("<tr class='odd'>")
print("<td>")

print("<table border='1'>")
print("<caption>10 Words Occurring Most Often</caption>")
print("<tbody>")
print("<tr class='odd'>")
print("<th>No of occurrences</th>")
print("<th>Words</th>")
print("</tr>")

count=1
for key,value in max_dict.items():
    if(count<11):
        print("<tr class='odd'>")
        print("<th>"+str(value)+"</th>")
        print("<th>"+key+"</th>")
        print("</tr>")
    count= count+1





print("</tbody>")
print("</table>")
print("</td>")

print("<td>")
print("<table border='1'>")
print("<caption>10 Words Occurring Least Often</caption>")
print("<tbody>")
print("<tr class='odd'>")
print("<th>No of occurrences</th>")
print("<th>Words</th>")
print("</tr>")

count=1
for key,value in min_dict.items():
    if(count<11):
        print("<tr class='odd'>")
        print("<th>"+str(value)+"</th>")
        print("<th>"+key+"</th>")
        print("</tr>")
    count= count+1


print("</tbody>")
print("</table>")
print("</td>")


print("</tbody>")
print("</table>")




