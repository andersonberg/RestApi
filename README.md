RestApi
=======

Interface Rest utilizando o Django com Tastypie

Exemplo de POST:

curl --dump-header - -H "Content-Type: application/json" -X POST http://localhost:8000/api/experimento/ -d '{"name": "Experimento 1", "alternativas": [{"url": "testeA.com", "peso":1},{"url": "testeB.com", "peso": 2}]}'