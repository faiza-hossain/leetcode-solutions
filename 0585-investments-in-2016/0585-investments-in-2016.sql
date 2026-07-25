# Write your MySQL query statement below
select round(sum(t.tiv_2016),2) as tiv_2016
from(
select pid,tiv_2016
from Insurance
where tiv_2015 IN(select distinct tiv_2015
from Insurance
group by tiv_2015
having count(*)>1)
and (lat,lon) in
(select lat,lon
 from Insurance
 group by lat,lon
 having count(*)=1)) as t
