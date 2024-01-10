-- 코드를 입력하세요

select base.flavor
from (
    SELECT f.flavor, f.total_order + j.total_order_j as total_order_sum
    FROM first_half f
    left JOIN (
        select flavor, sum(total_order) as total_order_j
        from july
        group by flavor
    ) j
    on f.flavor = j.flavor
) base
order by base.total_order_sum desc
limit 3

