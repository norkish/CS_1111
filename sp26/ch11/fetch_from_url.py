import urllib.request
import ssl

context = ssl._create_unverified_context()

def retrieve_page(url):
    """ Retrieve the contents of a web page.
    """
    my_socket = urllib.request.urlopen(url, context=context)
    data = my_socket.read()
    return data

the_text = retrieve_page("https://raw.githubusercontent.com/norkish/CS_1111/refs/heads/main/f25/ch2/birthday.py")
print(the_text)
