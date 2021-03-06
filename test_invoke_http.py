# test_invoke_http.py
from invoke import invoke_http

# invoke book microservice to get all books
results = invoke_http("http://localhost:5005/restaurant", method='GET')

print( type(results) )
print()
print( results )

# invoke book microservice to create a book
restaurantID = '2'
book_details = { "restaurantName": "McDonalds", "restaurantContact": 91234567, "restaurantAddress": "ESD", "postalCode":123456 }
create_results = invoke_http(
        "http://localhost:5005/restaurant/" + restaurantID, method='POST', 
        json=book_details
    )

print()
print( create_results )
