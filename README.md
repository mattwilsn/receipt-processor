# receipt-processor

This was built with the following

`Docker version 20.10.8, build 3967b7d`
`Python 3.11.11`

## How to run w/ docker

`docker build -t receipt-processor .`
`docker run -p 5000:5000 receipt-processor`

## How to run e2e tests

`pip install -r requirements.txt`
`cd tests`
`python -m unittest e2e.py`

## Available endpoints

**/receipts/process**  

 `{"id":"6aa32256-7d61-4164-944d-3f6810db815e"}` |

**/receipts/{ID}/points**

`{"points":28}` |

### curl examples

receipts/process

     curl --header "Content-Type: application/json" --request POST --data '{"retailer": "Target","purchaseDate": "2022-01-01","purchaseTime": "13:01","items": [{"shortDescription": "Mountain Dew 12PK","price": "6.49"},{"shortDescription": "Emils Cheese Pizza","price": "12.25"},{"shortDescription": "Knorr Creamy Chicken","price": "1.26"},{"shortDescription": "Doritos Nacho Cheese","price": "3.35"},{"shortDescription": " Klarbrunn 12-PK 12 FL OZ ","price": "12.00"}],"total": "35.35"}' http://localhost:5000/receipts/process

/receipts/{ID}/points

     curl --header "Content-Type: application/json" --request GET http://localhost:5000/receipts/{ID}/points
