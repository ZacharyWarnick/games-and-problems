
'''
File: josephus.py

Description: solves the josephus problem with linked list
'''


class Link(object):
	def __init__ ( self,data = None ,next = None ): 
		self.data = data
		self.next = next

class CircularList(object):
	# Constructor
	def __init__ ( self):
		self.first = None


	# Insert an element (value) in the list
	def insert ( self, data):
		newLink = Link(data)

		if self.first == None:
			self.first = newLink
			newLink.next = self.first
			self. first = newLink
			return

		current = self.first

		while current.next != self.first:
			current = current.next


		current.next = newLink

		newLink.next = self.first

		newLink.previous = current

	def find(self,data):

		if self.first == None:

			current = self.first

		while current.data == self.first:

			if current.next == self.first:
				return None
			else:
				current = current.next

		return current

		def len(self):

			if self.first == None:
				return 0

			count = 1
			current = self.first

			while current != self.first:

				count += 1
				current = current.next

			return count

	# Delete a link with a given data (value)
	def delete ( self, data ):

			if self.first == None:
				return None

			current = self.first
			previous = self.first

			while previous.next != self.first:
				previous = previous.next

			while current.data != data:
				if current.next == self.first:
					return None

				previous = current
				current = current.next

			if current == self.first:
				if self.first == self.first.next:
					self.first = None
					return current

				else:
					self.first = current.next

			previous.next = current.next

			return current

	def delete_after ( self, start, n ):
		if self.first == None:
			return None
		current = self.first

		while (current.data != start):
			current = current.next

		count = 1
		while (count != n):
			current = current.next
			count += 1

		self.delete(current.data)


		print(current.data, end = " ")

		return current.next

	def __str__ ( self ):
		output = ""

		if self.first == None:
			return None

		else:
			current = self.first

			while current.next != self.first:
				output += (str(current.data) + "\n")
				current = current.next

		return output
			


def main():

	in_file = open("./josephus.txt", "r")

	num_soldiers = int(in_file.readline())

	starting = int(in_file.readline())

	eliminations = int(in_file.readline())

	in_file.close()

	ouro = CircularList()

	for n in range(1,num_soldiers+1):
		ouro.insert(n)



	for i in range(num_soldiers):
		#delete the item, set start count equal to the memory address of the next link
		starting = ouro.delete_after(starting, eliminations)
		#pull the data from this memory address for the next iteration
		starting = starting.data

	print()
	return (ouro)

if __name__ == '__main__':
  main()