# Assessment

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
3. Create a new Order ("orders/")
    ``` 
  {
    "firstName" : "Dhrubo",
    "lastName" : "Hasan",
    "email" : "DHR@mail.com",
    "item" : "Medicine"
}
```
5. Find day from DOB ("/customers/{customer_id}/birthday")
  sample response:
  ```
  {
    "DOB": "11-29-1993",
    "day": "Monday"
    }
    ```
6. Find continent ("/customers/{customer_id}/continent")
sample response:
  ```
  {
    "country": "Bahamas",
    "continent": "NA"
    }
    ```
7. 
8. 
