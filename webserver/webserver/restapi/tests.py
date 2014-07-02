from django.test import TestCase
from tastypie.test import ResourceTestCase
from webserver.restapi.api import *
from webserver.restapi.models import User, Experimento, Alternativa


class UserResourceTest(ResourceTestCase):

    def setUp(self):
        """ Setup inicial dos testes da classe User. Cria um novo usuário para ser utilizado nos testes. """
        super(UserResourceTest, self).setUp()

        #Dados que serão enviados em requisições POST
        self.post_data = {'username': 'Anderson'}
        #Cadastra um novo usuário
        self.api_client.post('/api/user/', format='json', data=self.post_data)
        self.user_1 = User.objects.get(slug='anderson')
        self.detail_url = '/api/user/{0}/'.format(self.user_1.slug)

    def test_post_list(self):
        """ Testa a função POST """
        user_2 = {'username': 'Berg'}
        #verifica se o usuário foi criado.
        self.assertHttpCreated(self.api_client.post('/api/user/', format='json', data=user_2))
        #verifica se foi adicionado um usuário
        self.assertEqual(User.objects.count(), 2)

    def test_get_detail_json(self):
        """ Testa a função GET para detalhes do usuário.
        """
        resp = self.api_client.get(self.detail_url, format='json')
        #verifica se a resposta é um JSON válido
        self.assertValidJSONResponse(resp)
        #verifica se a resposta do GET é a esperada
        self.assertEqual(self.deserialize(resp)['username'], 'Anderson')

    def test_patch_detail(self):
        """ Testa a atualização de um ou mais atributos de um usuário.
        """
        original_data = self.deserialize(self.api_client.get(self.detail_url, format='json'))
        #cria uma cópia do dado original para ser modificado
        new_data = original_data.copy()
        new_data['username'] = 'Anderson Berg'

        self.assertEqual(User.objects.count(), 1)
        #realiza a requisição e verifica se foi aceita
        self.assertHttpAccepted(self.api_client.patch(self.detail_url, format='json', data=new_data))
        #verifica se não foi adicionado nenhum usuário novo
        self.assertEqual(User.objects.count(), 1)
        #verifica se a operação foi realizada corretamente
        self.assertEqual(User.objects.get(id=1).username, 'Anderson Berg')

    def test_put_list(self):
        """ Testa a função PUT para atualizar todos os atributos de um usuário.
        """
        original_data = self.deserialize(self.api_client.get(self.detail_url, format='json'))
        new_data = original_data.copy()
        new_data['username'] = 'Anderson Dantas'
        new_data['alternativa'] = {'url': 'testeE.com', 'peso': 4}

        #realiza a requisição e verifica se foi aceita
        self.assertHttpAccepted(self.api_client.put(self.detail_url, format='json', data=new_data))
        #verifica as informações modificadas
        self.assertEqual(User.objects.get(id=1).username, 'Anderson Dantas')
        #o slug não é modificado, pois faz parte da url
        self.assertEqual(User.objects.get(id=1).slug, 'anderson')


class ExperimentoResourceTest(ResourceTestCase):

    def setUp(self):
        """ Setup inicial dos testes da classe Experimento.
        Cria um novo experimento e suas alternativas para serem utilizados nos testes.
        """
        super(ExperimentoResourceTest, self).setUp()

        alternativa_1 = {'url': 'testeA.com', 'peso': 1}
        alternativa_2 = {'url': 'testeB.com', 'peso': 2}

        self.post_data = {'name': 'Experimento 1', 'alternativas': [alternativa_1, alternativa_2]}
        self.api_client.post('/api/experimento/', format='json', data=self.post_data)
        self.experimento_1 = Experimento.objects.get(slug='experimento_1')
        self.detail_url = '/api/experimento/{0}/'.format(self.experimento_1.slug)

    def test_post_list(self):
        """ Testa a função POST para criar um novo experimento.
        """
        alternativa_c = {'url': 'testeC.com', 'peso': 1}
        alternativa_d = {'url': 'testeD.com', 'peso': 2}

        experimento_2 = {'name': 'Experimento 2', 'alternativas': [alternativa_c, alternativa_d]}
        #verifica se o experimento foi criado.
        self.assertHttpCreated(self.api_client.post('/api/experimento/', format='json', data=experimento_2))
        #verifica se foi adicionado um experimento
        self.assertEqual(Experimento.objects.count(), 2)

    def test_get_detail_json(self):
        """ Testa a função GET para exibir detalhes de um experimento.
        """
        resp = self.api_client.get(self.detail_url, format='json')
        #verifica se a resposta é um JSON válido
        self.assertValidJSONResponse(resp)
        #verifica se a resposta do GET é a esperada
        self.assertEqual(self.deserialize(resp)['name'], 'Experimento 1')

    def test_patch_detail(self):
        """ Testa a função PATCH para atualizar um ou mais atributos de um experimento.
        """
        original_data = self.deserialize(self.api_client.get(self.detail_url, format='json'))
        #cria uma cópia do dado original para ser modificado
        new_data = original_data.copy()
        new_data['name'] = 'Experimento 3'

        self.assertEqual(Experimento.objects.count(), 1)
        #realiza a requisição e verifica se foi aceita
        self.assertHttpAccepted(self.api_client.patch(self.detail_url, format='json', data=new_data))
        #verifica se não foi adicionado nenhum experimento novo
        self.assertEqual(Experimento.objects.count(), 1)
        #verifica se a operação foi realizada corretamente
        self.assertEqual(Experimento.objects.get(id=1).name, 'Experimento 3')

    def test_put_list(self):
        """ Testa a função PUT para atualizar todos os atributos de um experimento.
        """
        alternativa_x = {'url': 'testeX.com', 'peso': 3}
        alternativa_z = {'url': 'testeZ.com', 'peso': 4}

        original_data = self.deserialize(self.api_client.get(self.detail_url, format='json'))
        new_data = original_data.copy()
        new_data['name'] = 'Experimento X'
        new_data['alternativas'] = [alternativa_x, alternativa_z]

        #realiza a requisição e verifica se foi aceita
        self.assertHttpAccepted(self.api_client.put(self.detail_url, format='json', data=new_data))
        #verifica as informações modificadas
        self.assertEqual(Experimento.objects.get(id=1).name, 'Experimento X')
        #o slug não é modificado, pois faz parte da url
        self.assertEqual(Experimento.objects.get(id=1).slug, 'experimento_1')
