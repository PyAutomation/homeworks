def autocomplete(pattern, words):
	def helper(str):
		L = [ch for ch in str if ch.isalpha()]
		return ''.join(L)
	return [word for word in words if \
			helper(word.lower()).startswith(pattern.lower())][:5]
