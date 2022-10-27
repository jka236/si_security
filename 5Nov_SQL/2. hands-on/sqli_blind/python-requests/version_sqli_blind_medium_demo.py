import requests
from bs4 import BeautifulSoup

LIMIT = 100
PHPSESSID = "vj4j0b0s5vo65mdd54ohullaq4"
SECURITY = "medium"
HEADER = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1"}

def get_db_version_len():
    '''Send a SQL attack and get the length of the db version'''
    # Loop until SQL command return True. Try untill 100. If not found, raise an error
    version_len = 0
    while True:
        version_len += 1
        # url = 
        # burp_data =
        # cookies =
        # response = 
        
        # Parse response HTML and check if it returned True
        html_doc = response.content.decode()
        soup = BeautifulSoup(html_doc, 'html.parser')
        # if soup.pre.text == :
            return version_len
        if version_len >= 100:
            raise ValueError(f'Tried {version_len} time but table len not found')   
        
def get_db_ver_char_ascii(digit):
    '''Send a SQL attack and get a char of the db version'''
    target_ascii = 0
    while True:
        target_ascii += 1
        # url = 
        # burp_data =
        # cookies = 
        # response = 
        
        # Parse response HTML and check if it returned True
        html_doc = response.content.decode()
        soup = BeautifulSoup(html_doc, 'html.parser')
        # if soup.pre.text == :
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
    print(db_version_len)
    db_version = get_db_ver(db_version_len)
    print(db_version)
    
    