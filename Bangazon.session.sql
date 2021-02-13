SELECT
    p.id,
    p.deleted,
    p.name,
    p.price,
    p.description,
    p.quantity,
    p.created_date,
    p.location,
    p.image_path,
    p.category_id,
    p.customer_id
FROM
    bangazonapi_product p
WHERE
    p.price <= 999