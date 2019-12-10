curl google.com

curl -i google.com

curl http://dummy.restapiexample.com/api/v1/employees

curl http://dummy.restapiexample.com/api/v1/employee/121829

curl -i -X DELETE http://dummy.restapiexample.com/api/v1/delete/126936

curl -i -d “{\"name\":\"Grace\",\"salary\":\"100000\",\"age\":\"22\"}” -H “Content-Type: application/json” -X POST http://dummy.restapiexample.com/api/v1/create

curl -d “{\"name\":\"Mary\",\"salary\":\"12000\",\"age\":99}” -H “Content-Type: application/json” -X PUT http://dummy.restapiexample.com/api/v1/update/121829