cURL command for READ operation
```
curl -X GET http://192.168.1.18:8000/get-notes
```

cURL command for CREATE operation
```
curl -X POST http://192.168.1.18:8000/create-note \
   -H 'Content-Type: application/json' \
   -d '{"title":"Hello World", "note":"ABCD"}'
```

cURL command for DELETE operation
```
curl -X DELETE http://192.168.1.18:8000/delete-note \
   -H 'Content-Type: application/json' \
   -d '{"title":"Hello World"}'
```

cURL command for UPDATE operation
```
curl -X PUT http://192.168.1.18:8000/update-note \
   -H 'Content-Type: application/json' \
   -d '{"title":"Something Else", "note":"Another Content"}'
```

cURL command for CREATE file operation
```
curl -X POST http://192.168.1.18:8000/create-picture \
   -F 'attachment=@/tmp/pict.jpeg'
```