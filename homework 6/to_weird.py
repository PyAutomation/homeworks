def to_weird(str):
	def helper(word):
		L = list(word)
		for i in xrange(0, len(word), 2):
			L[i] = L[i].upper()
		return ''.join(L)
	words = [helper(word) for word in str.split()]
	return '-'.join(words)
