class Crowdmap (object):
	def _init_(self,init_list):
	self.list = init_list
	
	def get_all_posts_for(self,param):
		return [post for post in self.list if.find(param) !=-1]