class card():
	"""This creates a card object"""
	suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
	'8', '9', '10', 'Jack', 'Queen', 'King']
	def __init__(self,rank=0,suite=2):
		self.rank=rank
		self.suite=suite
	def __str__(self):
		return f"The rank is {card.rank_names[self.rank]} and the suite is {card.suit_names[self.suite]}"
ace_of_spade=card()
print(ace_of_spade)
