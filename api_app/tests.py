
import json
from django.test import TestCase, Client
from django.http import HttpResponse


from api_app.models import Criature
from django.db.models   import QuerySet

# https://docs.djangoproject.com/en/4.1/topics/testing/tools/
# Create your tests here.
class VerificationCriatureTestCase(TestCase):
    """Test case setup"""
    def setUp(self):
        
        self.criature = Criature.objects.create(
            id_evolution= 2500, 
            evolution= ["evolutionbasic", "evolutionplus", "evolution x"], 
            name= "pokemonTest", 
            height= 56,
            weight= 65,
            base_stats= "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin vestibulum libero ipsum, eu tincidunt velit scelerisque a. Cras iaculis, nisl ut posuere rhoncus, quam tellus sollicitudin tortor, et condimentum quam leo vel turpis. Maecenas nec tincidunt lectus. Pellentesque porttitor eu nunc non cursus. Sed sit amet tempus mauris, nec mollis sapien. Donec pellentesque consequat pulvinar. Cras varius ac purus nec aliquet. Donec sit amet imperdiet odio."
        )
        self.c = Client()


    """Test case ping url"""
    def test_index_url(self):
        response = self.c.get('/ping/')
        

        self.assertEqual(response.content, b"pong")

    """Test case db with a criature"""
    def test_code_criature_exist(self):
        criature=Criature.objects.filter(name="pokemonTest")

        self.assertIsNotNone(criature)
        self.assertIsInstance(criature, QuerySet)

    """Test case index ulr"""
    def test_index_url(self):
        response = self.c.get('/')
        print(response.content)
        print(bytes.decode(response.content))

        # import pdb; pdb.set_trace()
        self.assertEqual(response.content, b"Hello Pokemon view.")
        
        self.assertContains(response, 'Hello', status_code=200)

    """Test case search url"""
    def test_search_url(self):
        response = self.c.get('/search/pokemonTest')
        # 

        # self.assertEqual(response.status_code, 200)
        print(response.content)
        print(bytes.decode(response.content))

        # import pdb; pdb.set_trace()
        # self.assertEqual(response.content, b"Hello Pokemon view.")
        
        self.assertContains(response, 'Evolution', status_code=200)
        self.assertContains(response, '"Id": 2500', status_code=200)




