-- fans
SELECT origin, SUM(fans) AS nb_fans from metal_bands group by origin order by nb_fans DESC;