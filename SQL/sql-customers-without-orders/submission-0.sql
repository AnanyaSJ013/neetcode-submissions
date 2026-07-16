-- Write your query below
Select name from customers
Where id Not In(Select customer_id from orders); 