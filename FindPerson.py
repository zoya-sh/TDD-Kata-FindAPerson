import unittest
from Crowdmap import Crowdmap

class Crowdmap(object):
	def get_all_posts_from(self, param)
	return ["Or"]

class FindAPersonTestes(unittest.TestCase):
	def stUp(self):
		self.crowdmap =  Crowdmap(["I......"])
	
	def	test_getAllPostsForName(self):
		posts = self.crowdmap.get_all_Posts_for("Or")
		self.assertIn("Or",posts)
	def	test_getAllPostsForMissingName(self):
		posts = self.crowdmap.get_all_Posts_for("Or2")
		self.assertIn("Or2",posts)
	def test_homework_example(self):
		posts = self.crowdmap.get_all_Posts_for("Or2")
		self.assertIn("Or A.",posts)	
			
		
if _name_ == '_main_':
	unittest.main()