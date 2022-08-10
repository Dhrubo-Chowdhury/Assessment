# Assessment
ERD:
![image](https://user-images.githubusercontent.com/48079397/183977894-03b25eb0-cd44-441d-a013-da2072bbaae7.png)


Endpints:
1. Create a new Customer ("/customers/")
Sample request:
``` 
{
    "firstName" : "Dhrubo",
    "lastName" : "Hasan",
    "dateOfBirth" : "11-29-1996",
    "email" : "DHR@mail.com",
    "city" : "Sunnyvale",
    "country" : "USA"
}
```
2. Create a new Order ("/orders/")
``` 
{
    "firstName" : "Dhrubo",
    "lastName" : "Hasan",
    "email" : "DHR@mail.com",
    "item" : "Medicine"
}
```
3. Find day from DOB ("/customers/{customer_id}/birthday")
sample response:
```
{
    "DOB": "11-29-1993",
    "day": "Monday"
 }
```
4. Find continent ("/customers/{customer_id}/continent")
sample response:
```
{
    "country": "Bahamas",
    "continent": "NA"
}
```
