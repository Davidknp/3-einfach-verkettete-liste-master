class OperatingSystem:
	# Konstruktor
	def __init__(self, name=None, date=None):
		self.name = name
		self.releaseDate = date
		self.next = None

class OSTimeline:
	# Konstruktor
	def __init__(self):
		self.head = None

	# Methode, die die Timeline durchläuft und eine Liste der enthaltenen Betriebssysteme zurückgibt
	# ACHTUNG: Ändern Sie diese Methode nicht, da Ihnen die Student-Test-Suite ansonsten ein falsches Ergebnis liefern kann!
	def traverse(self):
		L = []
		currentNode = self.head
		while currentNode is not None:
			L.append((currentNode.name, currentNode.releaseDate))
			currentNode = currentNode.next
		return L

	# Methode, die ein neues Element in die Timeline einfügt
	def insert(self, name, releaseDate):
		# Erstelle ein neues Objekt der Klasse OperatingSystem
		newOS = OperatingSystem(name, releaseDate)

		# Durchlaufe die Timeline beginnend am Kopf
		currentNode = self.head
		# Fall 1: Prüfe, ob OS als neuer Kopf eingesetzt werden muss
		if (newOS.releaseDate <= currentNode.releaseDate):
			if newOS.releaseDate == currentNode.releaseDate:
				return False
			newOS.next = self.head
			self.head = newOS
			return True
		else:
			while currentNode.next is not None and currentNode.next.releaseDate < newOS.releaseDate:
				
				if newOS.releaseDate == currentNode.releaseDate:
					return False
				else:
					currentNode = currentNode.next

			newOS.next = currentNode.next
			currentNode.next = newOS 
			return True 
			
					


			
