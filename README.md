RestApi
=======

Implementação de uma API Rest para testes A/B utilizando o Django com Tastypie.

O Tastypie é um framework que provê uma API RESTful para Django. O Tastypie serializa a saída em diversos formatos, incluindo json, que utilizamos neste projeto.
Através da criação de objetos 'Resource', o Tastypie implementa formas de obter dados (GET), criar (POST) e modificar (PUT/PATCH) dados e excluir dados (DELETE).


Interagindo com a API
---------------------

Os exemplos a seguir usam o curl para realizar as requisições via linha de comando. Nestes exemplos, considere que a API

###Criando um novo experimento###

Para cadastrar um novo experimento e as respectivas alternativas execute o seguinte comando (as alternativas são criadas automaticamente):

<pre><code>
curl --dump-header --dump-header - -H "Content-Type: application/json" -X POST http://localhost:8000/api/experimento/ -d '{"name": "Experimento 1", "alternativas": [{"url": "testeA.com", "peso":1},{"url": "testeB.com", "peso": 2}]}'
</code></pre>

Passar o parâmetro --dump-header - é opcional, ele faz com que o curl responda com todos os cabeçalhos e códigos de status.

O cabeçalho "Content-Type" é importante, pois informa ao Tastypie que estamos enviando dados JSON serializados.

###Listando todos os experimentos###

<pre><code>
curl http://localhost:8001/api/experimento/
</code></pre>

###Listando os detalhes de um experimento específico###

<pre><code>
curl http://localhost:8001/api/experimento/experimento_1/
</code></pre>

###Criando um novo usuário###

Para criar um novo usuário, basta informar o 'username':

<pre><code>
curl --dump-header - -H "Content-Type: application/json" -X POST http://localhost:8000/api/user/ -d '{"username":"Usuario 1"}'
</code></pre>

###Listando todos os usuários###

<pre><code>
curl http://localhost:8001/api/user/
</code></pre>

###Requisitanto um sorteio para um usuário específico:###

Para requisitar um sorteio de um experimento para um usuário específico, o modelo de requisição é o seguinte:

<pre><code>
curl http://localhost:8000/api/experimento/experimento_1/user/?id=1
</code></pre>

A adição de '/user/' à URL é para que não haja conflito com a url para fazer a requisição dos detalhes de um experimento específico.

Se o usuário já possui uma alternativa sorteada, será retornada esta alternativa, senão será sorteada uma nova.