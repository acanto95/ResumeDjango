
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

# Define this after the ModelTestCase
class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.MainInfo_data = {'name': 'Canto'}
        self.response = self.client.post(
            reverse('create'),
            self.MainInfo_data,
            format="json")

    def test_api_can_create_a_maininfo(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


    def test_api_can_get_a_MainInfo(self):
        """Test the api can get a given MainInfo."""
        MainInfo = MainInfo.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': MainInfo.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, MainInfo)

    def test_api_can_update_MainInfo(self):
        """Test the api can update a given MainInfo."""
        change_MainInfo = {'name': 'Something new'}
        res = self.client.put(
            reverse('details', kwargs={'pk': MainInfo.id}),
            change_MainInfo, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_MainInfo(self):
        """Test the api can delete a MainInfo."""
        MainInfo = MainInfo.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': MainInfo.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)