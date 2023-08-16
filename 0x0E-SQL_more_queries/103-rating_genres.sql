--  script that lists all genres in the database
-- hbtn_0d_tvshows_rate by their rating.
SELECT g.name AS genre_name, SUM(sr.rate) AS rating_sum
FROM tv_genres g
JOIN tv_show_genres sg ON g.id = sg.genre_id
JOIN tv_show_ratings sr ON sg.show_id = sr.show_id
GROUP BY g.name
ORDER BY rating_sum DESC;
