SELECT x,y,z,
    CASE 
        WHEN 
        x+y>z and x+z>y and y+z > x THEN 'Yes'
        Else 'No'
    End as triangle    
FROM triangle
