import sqlite3
from django.shortcuts import render
from bangazonapi.models import Product
from bangazonreports.views import Connection


def inexpensiveproduct_list(request):

    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
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
            """)

            dataset = db_cursor.fetchall()

            inexpensive_products = {}

            for row in dataset:
                product = Product()
                product.deleted = row["deleted"]
                product.name = row["name"]
                product.price = row["price"]
                product.description = row["description"]
                product.quantity = row["quantity"]
                product.created_date = row["created_date"]
                product.location = row["location"]
                product.image_path = row["image_path"]
                product.category_id = row["category_id"]
                product.customer_id = row["customer_id"]

                inexpensive_products.append(product)

        list_of_inexpensive_products = inexpensive_products.values()

        template = 'users/list_with_inexpensive_products.html'
        context = {
            'inexpensiveproduct_list': list_of_inexpensive_products
        }

        return render(request, template, context)