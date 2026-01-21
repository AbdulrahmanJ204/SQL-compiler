USE AdventureWorks2022;
GO

SELECT
    ProductNumber,
    Name,
    ListPrice,
    PriceCategory =
        CASE
            WHEN ListPrice > 1000 THEN 'High-end'
            ELSE
                CASE ProductLine
                    WHEN 'R' THEN
                        CASE
                            WHEN ListPrice > 500 THEN 'Premium Road'
                            ELSE 'Standard Road'
                        END
                    WHEN 'M' THEN
                        CASE
                            WHEN ListPrice > 500 THEN 'Premium Mountain'
                            ELSE 'Standard Mountain'
                        END
                    WHEN 'T' THEN 'Touring'
                    ELSE 'Other'
                END
        END
FROM Production.Product
ORDER BY ListPrice DESC;