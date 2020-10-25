주어진 정보를 활용하여 작성된 SQL 문과 대응하는 ORM 문을 작성하고 실행해보자.

#### Table Name : users

| name       | data type   |
| ---------- | ----------- |
| id         | integer(pk) |
| first_name | text        |
| last_name  | text        |
| age        | integer     |
| country    | text        |
| phone      | text        |
| balance    | integer     |

---

1. user 테이블 전체 데이터를 조회하시오.

```sql
SELECT * FROM users_user;
```

```python

```

2. id가 19인 사림의 age를 조회하시오.

```sql
SELECT age FROM users_user
WHERE id = 19;
```

```python

```

3. 모든 사람의 age를 조회하시오.

```sql
SELECT age FROM users_user;
```

```python

```

4. age가 40 이하인 사림들의 id와 balance를 조회하시오.

```sql
SELECT id, balance FROM users_user
WHERE age <= 40;
```

```python

```

5. last_name이 ‘김’이고 balance가 500 이상인 사람들의 first_name을 조회하시오.

```sql
SELECT first_name FROM users_user
WHERE last_name = '김' AND balance >= 500;
```

```python

```

6. first_name이 ‘수’로 끝나면서 행정구역이 경기도인 사람들의 balance를 조회하시오.

```sql
SELECT balance FROM users_user
WHERE first_name LIKE '%수' AND country = '경기도';
```

```python

```

7. balance가 2000 이상이거나 age가 40 이하인 사람의 총 인원수를 구하시오.

```sql
SELECT COUNT(*) FROM users_user
WHERE balance >= 2000 OR age <= 40;
```

```python

```

8. phone 앞자리가 ‘010’으로 시작하는 사람의 총원을 구하시오.

```SQL
SELECT COUNT(*) FROM users_user
WHERE phone LIKE '010%';
```

```python

```

9. 이름이 ‘김옥자’인 사람의 행정구역을 경기도로 수정하시오.

```sql
UPDATE users_user SET country = '경기도'
WHERE first_name = '옥자' AND last_name = '김';

SELECT country FROM users_user
WHERE first_name = '옥자' AND last_name = '김';
```

```python

```

10. 이름이 ‘백진호’인 사람을 삭제하시오.

```sql
DELETE FROM users_user
WHERE first_name = '진호' AND last_name = '백';
```

```python

```

11. balance를 기준으로 상위 4명의 first_name, last_name, balance를 조회하시오.

```sql
SELECT first_name, last_name, balance FROM users_user
ORDER BY balance DESC LIMIT 4;
```

```python

```

12. phone에 ‘123’을 포함하고 age가 30미만인 정보를 조회하시오.

```sql
SELECT * FROM users_user
WHERE age < 30 AND phone LIKE '%123%';
```

```python

```

13. phone이 ‘010’으로 시작하는 사람들의 행정 구역을 중복 없이 조회하시오.

```sql
SELECT DISTINCT country FROM users_user
WHERE phone LIKE '010%';
```

```python

```

14. 모든 인원의 평균 age를 구하시오.

```sql
SELECT AVG(age) FROM users_user;
```

```python

```

15. 박씨의 평균 balance를 구하시오.

```sql
SELECT AVG(balance) FROM users_user
WHERE last_name = '박';
```

```python

```

16. 경상북도에 사는 사람 중 가장 많은 balance의 액수를 구하시오.

```sql
SELECT MAX(balance) FROM users_user
WHERE country = '경상북도';
```

```python

```

17. 제주특별자치도에 사는 사람 중 balance가 가장 많은 사람의 first_name을 구하시오.

```sql
SELECT first_name FROM users_user
WHERE country = '제주특별자치도' 
ORDER BY balance DESC LIMIT 1;
```

```python

```





* **주의! 무단전재나 재배포는 금합니다.**