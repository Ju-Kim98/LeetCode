# Write your MySQL query statement below

SELECT 
    product_id
FROM
    Products
WHERE
    low_fats = 'Y' AND recyclable = 'Y'


-- import pandas as pd

-- def find_products(products: pd.DataFrame) -> pd.DataFrame:
--     df = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
--     df = df[['product_id']]
    
--     return df
