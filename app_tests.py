from app import app
import unittest 

class MyCookbook(unittest.TestCase):
    # initialization logic for the test suite declared in the test module
    # code that is executed before all tests in one test run
    @classmethod
    def setUpClass(cls):
        pass
    
    # clean up logic for the test suite declared in the test module
    # code that is executed after all tests in one test run
    @classmethod
    def tearDownClass(cls):
        pass
    
    # initialization logic
    # code that is executed before each test
    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True
    
    # clean up logic
    # code that is executed after each test
    def tearDown(self):
        pass
    
    
    #Tests can be found here
    """
    #Test OK
    def test_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
    
    #Test OK
    def test_status_code(self):
        result = self.app.get('/session_user')
        self.assertEqual(result.status_code, 200)
    
    #Test OK
    def test_status_code(self):
        result = self.app.get('/get_username')
        self.assertEqual(result.status_code, 302)
    
    #Tests OK
    def test_status_code(self):
        result = self.app.get('/get_recipes')
        self.assertEqual(result.status_code, 200)
        
    def test_status_code(self):
        result = self.app.get('/get_recipes')
        self.assertEqual(result.status_code, 302)
    
    #Tests OK
    def test_status_code(self):
        result = self.app.get('/show_recipe/<recipe_id>')
        self.assertEqual(result.status_code, 302)
    
    #Test OK
    def test_status_code(self):
        result = self.app.get('/breakfast_recipes')
        self.assertEqual(result.status_code, 302)
    
    #Test OK
    def test_status_code(self):
        result = self.app.get('/lucnh_recipes')
        self.assertEqual(result.status_code, 302)
    
    #Test OK
    def test_status_code(self):
        result = self.app.get('/dinner_recipes')
        self.assertEqual(result.status_code, 302)
    
    #Test OK
    def test_status_code(self):
        result = self.app.get('/contribute_recipes')
        self.assertEqual(result.status_code, 302)
    
    #Test OK
    def test_status_code(self):
        result = self.app.post('/add_recipes')
        self.assertEqual(result.status_code, 302)
        
    #Test OK
    def test_status_code(self):
        result = self.app.get('/edit_page')
        self.assertEqual(result.status_code, 302)
        
    #Test OK
    def test_status_code(self):
        result = self.app.get('/delete_page')
        self.assertEqual(result.status_code, 302)
        
    #Test OK
    def test_status_code(self):
        result = self.app.get('/delete_recipe/<recipe_id>')
        self.assertEqual(result.status_code, 302)
        
    #Test OK
    def test_status_code(self):
        result = self.app.get('/edit_page_form/<recipe_id>')
        self.assertEqual(result.status_code, 302)
        
    #Test OK
    def test_status_code(self):
        result = self.app.post('/edit_recipe/<recipe_id>')
        self.assertEqual(result.status_code, 302)
    
    #Test OK
    def test_status_code(self):
        result = self.app.post('/upvote/<recipe_id>')
        self.assertEqual(result.status_code, 302)
        
    #Test OK
    def test_status_code(self):
        result = self.app.post('/downvote/<recipe_id>')
        self.assertEqual(result.status_code, 302)
        
    #Test OK
    with app.test_client() as c:
        with c.session_transaction() as sess:
            sess['a_key'] = 'a value'
    """
    
# runs the unit tests in the module
if __name__ == "__main__":
    unittest.main
    
    