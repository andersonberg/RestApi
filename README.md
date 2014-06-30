RestApi
=======

Implementação de uma API Rest para testes A/B utilizando o Django com Tastypie.

O Tastypie é um framework que provê uma API RESTful para Django. O Tastypie serializa a saída em diversos formatos, incluindo json, que utilizamos neste projeto.
Através da criação de objetos 'Resource', o Tastypie implementa formas de obter dados (GET), criar (POST) e modificar (PUT/PATCH) dados e excluir dados (DELETE).


Interagindo com a API
---------------------

Os exemplos a seguir usam o curl para realizar as requisições.

###Criando um novo experimento###

Para cadastrar um novo experimento e as respectivas alternativas execute o seguinte na linha de comando:

<pre><code>
curl --dump-header - -H "Content-Type: application/json" -X POST http://localhost:8000/api/experimento/ -d '{"name": "Experimento 1", "alternativas": [{"url": "testeA.com", "peso":1},{"url": "testeB.com", "peso": 2}]}'
</code></pre>

###Listando todos os experimentos###

<pre><code>
curl http://localhost:8001/api/experimento/
</code></pre>

###Listando os detalhes de um experimento específico###

<pre><code>
curl http://localhost:8001/api/experimento/experimento_1/
</code></pre>

###Exemplo de GET:###

Para requisitar um sorteio de um experimento para um usuário específico, o modelo de requisição http é o seguinte:

<pre><code>
http://localhost:8000/api/experimento/{slug_do_experimento}/user/?id={id_do_usuario}
</code></pre>

A adição de '/user/' à URL é para que não haja conflito com a url para fazer a requisição dos detalhes de um experimento específico.


Para saber mais sobre REST:
http://pt.wikipedia.org/wiki/REST