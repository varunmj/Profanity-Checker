import urllib

def read_text():
    quotes = open("C:\Users\intel\Desktop\Udacity python projects\profanity checker\document_with_profanity.txt")
    content_of_file = quotes.read()
    print(content_of_file)
    quotes.close()
    check_profanity(content_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output=connection.read()
    #print("the response from the profanity checker : "+output)
    connection.close()
    if "true" in output:
        print("profanity alert!!!")
    elif "false" in output:
        print("this document has no profanity")
    else:
        print("could not scan the document")
    
read_text()
