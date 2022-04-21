# code by Group 7 (Syakir Nu'aim)

# KMP String Matching Algorithm
def KMPMatch(text,pattern):

	# Define Counter
	pattern_index = 0	# Used to store previous longest prefix
	text_index = 0		# Used to store text index value
	current_prefix = 1	# Used to calculate iteration of pattern for prefix calculation

	# Set all initial prefix value to zero
	prefix = [0]*len(pattern)

	# Longest Prefix Calculation
	while current_prefix < len(pattern):

		# Prefix Match
		if(pattern[current_prefix] == pattern[pattern_index]):
			pattern_index+=1
			prefix[current_prefix] = pattern_index
			current_prefix += 1

		# Prefix Not Match
		else:
			# Check if contains remaining prefix
			if(pattern_index > 0):
				pattern_index = prefix[pattern_index-1]
			# No same prefix found, set as 0 and go to next character
			else:
				prefix[current_prefix] = 0
				current_prefix += 1

	# Reset Counter
	current_prefix = 0

	# Find String Match
	while text_index < len(text):
		# text at current index same as current pattern (character compare)
		if(pattern[current_prefix] == text[text_index]):
			current_prefix+=1
			text_index+=1

			# All pattern match with string at certain index
			if(current_prefix == len(pattern)):
				print("Match Found at Index:" + str(text_index-current_prefix))

				# Go to longest prefix location - refer prefix array value
				current_prefix = prefix[current_prefix-1]

		# Mismatch Found
		else:
			# Go to longest prefix location - refer prefix array value
			current_prefix = prefix[current_prefix-1]

			# Jump to next character on text if prefix table point to index 0
			if(current_prefix) <= 0:
				text_index += 1
				current_prefix = 0

# Test Program
text = "algorisfunalgoisgreat"
pattern = "fun"
print("For Pattern: " + pattern)
KMPMatch(text,pattern)

pattern = "algo"
print("For Pattern: " + pattern)
KMPMatch(text,pattern)
