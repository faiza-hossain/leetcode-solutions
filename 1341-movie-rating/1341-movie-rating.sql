# Write your MySQL query statement below
(select m.title results
 from Movies m
 join MovieRating mr on m.movie_id=mr.movie_id
 where mr.created_at between '2020-02-01' and '2020-02-29'
 group by m.movie_id,m.title
ORDER BY AVG(mr.rating) DESC, m.title ASC
 limit 1)
union all
 (SELECT u.name AS results
    FROM Users u
    JOIN MovieRating mr
        ON u.user_id = mr.user_id
    GROUP BY u.user_id, u.name
    ORDER BY COUNT(*) DESC, u.name ASC
    LIMIT 1)
