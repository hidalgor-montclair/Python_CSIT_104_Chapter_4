# Step 1: Define a string that represents an HTTP request
request_str = 'GET index.html HTTP/1.1'  # This string simulates an HTTP request made by a browser

# Step 2: Check if the substring '/1.1' is inside the request_str using the 'in' operator
# This checks if the request is using the HTTP 1.1 protocol
if '/1.1' in request_str:
    print('HTTP protocol 1.1')  # If found, print that HTTP 1.1 is being used

# Step 3: Check if 'HTTPS' is NOT inside the request_str using the 'not in' operator
# This checks if the request is missing the secure 'HTTPS' protocol
if 'HTTPS' not in request_str:
    print('Unsecured connection')  # If 'HTTPS' is not found, print that the connection is not secure
