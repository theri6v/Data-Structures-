'''Python program Online algorithm for checking palindrome in a stream'''

# d is the number of characters in input alphabet
d = 256

# q is a prime number used for evaluating Rabin Karp's
# Rolling hash
q = 103

def checkPalindromes(string):

	# Length of input string
	N = len(string)

	# A single character is always a palindrome
	print string[0] + " Yes"

	# Return if string has only one character
	if N == 1:
		return

	# Initialize first half reverse and second half for
	# as firstr and second characters
	firstr = ord(string[0]) % q
	second = ord(string[1]) % q

	h = 1
	i = 0
	j = 0

	# Now check for palindromes from second character
	# onward
	for i in xrange(1,N):

		# If the hash values of 'firstr' and 'second'
		# match, then only check individual characters
		if firstr == second:

			# Check if str[0..i] is palindrome using
			# simple character by character match
			for j in xrange(0,i/2):
				if string[j] != string[i-j]:
					break
			j += 1
			if j == i/2:
				print string[i] + " Yes"
			else:
				print string[i] + " No"
		else:
			print string[i] + " No"

		# Calculate hash values for next iteration.
		# Don't calculate hash for next characters if
		# this is the last character of string
		if i != N-1:

			# If i is even (next i is odd)
			if i % 2 == 0:

				# Add next character after first half at
				# beginning of 'firstr'
				h = (h*d) % q
				firstr = (firstr + h*ord(string[i/2]))%q

				# Add next character after second half at
				# the end of second half.
				second = (second*d + ord(string[i+1]))%q
			else:
				# If next i is odd (next i is even) then we
				# need not to change firstr, we need to remove
				# first character of second and append a
				# character to it.
				second = (d*(second + q - ord(string[(i+1)/2])*h)%q
							+ ord(string[i+1]))%q

# Driver program
txt = "aabaacaabaa"
checkPalindromes(txt)

