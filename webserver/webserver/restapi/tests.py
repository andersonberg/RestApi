from django.test import TestCase
from tastypie.test import ResourceTestCase
from webserver.restapi.api import *
from webserver.restapi.models import User


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

    def test_put_detail(self):
        original_data = self.deserialize(self.api_client.get(self.detail_url, format='json'))
        new_data = original_data.copy()
        new_data['username'] = 'Anderson Berg'

        self.assertEqual(User.objects.count(), 1)
        self.assertHttpAccepted(self.api_client.put(self.detail_url, format='json', data=new_data))
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get(id=1).username, 'Anderson Berg')
        self.assertEqual(User.objects.get(id=1).slug, 'anderson_berg')