from pyexpat import version_info
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

LIMIT = 100
PHPSESSID = "mrkmml3bsf05ik17m4u7du5gj7"
SECURITY = "low"

def get_db_version_len():
    '''Send a SQL attack and get the length of the db version'''

        
def get_db_ver_char_ascii(digit):
    '''Send a SQL attack and get a char of the db version'''
    target_ascii = 0
    while True:
        target_ascii += 1
        # base_url = 
        # query = 
        # url = 
        # cookies = 
        # response = 
        
        # Parse response HTML and check if it returned True
        html_doc = response.content.decode()
        soup = BeautifulSoup(html_doc, 'html.parser')
        # if soup.pre.text == 
            return chr(target_ascii)
        if target_ascii > 127:
            raise ValueError(f'char not found on {digit}')

def get_db_ver(name_len):
    table_name = ""
    for idx in range(1, name_len + 1):
        table_name += get_db_ver_char_ascii(idx)
    return table_name

if __name__ == "__main__":
    db_version_len = get_db_version_len()
    db_version = get_db_ver(db_version_len)
    print(db_version)

    
    