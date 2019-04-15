import urllib.request

def read_text():
    txt = open(r"", "r")
    content_of_txt= txt.read()
    #print(content_of_txt)
    txt.close()
    check_profanity(content_of_txt)

def check_profanity(txt_to_check):
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+txt_to_check)
    output = connection.read()
    print(output)
    connection.close()
    #if "true" in output:
    #    print("Profanity found")
    #elif "false" in output:
    #    print("Safe")
    #else:
    #    print("Could not scan document properly")
    
read_text()
