from django.test import TestCase
from tastypie.test import ResourceTestCase
from webserver.restapi.api import *
from webserver.restapi.models import User, Experimento, Alternativa


class UserResourceTest(ResourceTestCase):

    def setUp(self):
        super(UserResourceTest, self).setUp()

        self.post_data = {'username': 'Anderson'}
        self.api_client.post('/api/user/', format='json', data=self.post_data)
        self.user_1 = User.objects.get(slug='anderson')
        self.detail_url = '/api/user/{0}/'.format(self.user_1.slug)

    def test_post_list(self):
        user_2 = {'username': 'Berg'}
        self.assertHttpCreated(self.api_client.post('/api/user/', format='json', data=user_2))
        self.assertEqual(User.objects.count(), 2)

    def test_get_detail_json(self):
        resp = self.api_client.get(self.detail_url, format='json')
        self.assertValidJSONResponse(resp)
        self.assertEqual(self.deserialize(resp)['username'], 'Anderson')

    def test_patch_detail(self):
        original_data = self.deserialize(self.api_client.get(self.detail_url, format='json'))
        new_data = original_data.copy()
        new_data['username'] = 'Anderson Berg'

        self.assertEqual(User.objects.count(), 1)
        self.assertHttpAccepted(self.api_client.patch(self.detail_url, format='json', data=new_data))
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get(id=1).username, 'Anderson Berg')

    def test_put_list(self):
        original_data = self.deserialize(self.api_client.get(self.detail_url, format='json'))
        new_data = original_data.copy()
        new_data['username'] = 'Anderson Dantas'
        new_data['alternativa'] = {'url': 'testeE.com', 'peso': 4}
        new_data['slug'] = 'anderson_dantas'

        self.assertHttpAccepted(self.api_client.patch(self.detail_url, format='json', data=new_data))
        self.assertEqual(User.objects.get(id=1).username, 'Anderson Dantas')
        self.assertEqual(User.objects.get(id=1).slug, 'anderson_dantas')


class ExperimentoResourceTest(ResourceTestCase):

    def setUp(self):
        super(ExperimentoResourceTest, self).setUp()

        alternativa_1 = {'url': 'testeA.com', 'peso': 1}
        alternativa_2 = {'url': 'testeB.com', 'peso': 2}

        self.post_data = {'name': 'Experimento 1', 'alternativas': [alternativa_1, alternativa_2]}
        self.api_client.post('/api/experimento/', format='json', data=self.post_data)
        self.experimento_1 = Experimento.objects.get(slug='experimento_1')
        self.detail_url = '/api/experimento/{0}/'.format(self.experimento_1.slug)

    def test_post_list(self):
        alternativa_c = {'url': 'testeC.com', 'peso': 1}
        alternativa_d = {'url': 'testeD.com', 'peso': 2}

        experimento_2 = {'name': 'Experimento 2', 'alternativas': [alternativa_c, alternativa_d]}
        self.assertHttpCreated(self.api_client.post('/api/experimento/', format='json', data=experimento_2))
        self.assertEqual(Experimento.objects.count(), 2)

    def test_get_detail_json(self):
        resp = self.api_client.get(self.detail_url, format='json')
        self.assertValidJSONResponse(resp)
        self.assertEqual(self.deserialize(resp)['name'], 'Experimento 1')

    def test_patch_detail(self):
        original_data = self.deserialize(self.api_client.get(self.detail_url, format='json'))
        new_data = original_data.copy()
        new_data['name'] = 'Experimento 3'

        self.assertEqual(Experimento.objects.count(), 1)
        self.assertHttpAccepted(self.api_client.patch(self.detail_url, format='json', data=new_data))
        self.assertEqual(Experimento.objects.count(), 1)
        self.assertEqual(Experimento.objects.get(id=1).name, 'Experimento 3')

    def test_put_list(self):
        alternativa_x = {'url': 'testeX.com', 'peso': 3}
        alternativa_z = {'url': 'testeZ.com', 'peso': 4}

        original_data = self.deserialize(self.api_client.get(self.detail_url, format='json'))
        new_data = original_data.copy()
        new_data['name'] = 'Experimento X'
        new_data['alternativas'] = [alternativa_x, alternativa_z]
        new_data['slug'] = 'experimento_x'

        self.assertHttpAccepted(self.api_client.patch(self.detail_url, format='json', data=new_data))
        self.assertEqual(Experimento.objects.get(slug='experimento_x').name, 'Experimento X')
        self.assertEqual(Experimento.objects.get(id=1).slug, 'experimento_x')
