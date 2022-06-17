from src.plans.BaseCategoryClass import BaseCategoryClass

class Music(BaseCategoryClass):
	def __init__(self):
		super().__init__('MUSIC', 100, 250)

class Video(BaseCategoryClass):
	def __init__(self):
		super().__init__('VIDEO', 200, 500)    
	
class Podcast(BaseCategoryClass):
	def __init__(self):
		super().__init__('PODCAST', 100, 300)    
	
