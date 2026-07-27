# Write your MySQL query statement below
select user_id ,name ,mail 
From Users
where mail REGEXP "^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode[.]com$"
and mail LIKE BINARY '%@leetcode.com'