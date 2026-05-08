class Solution:
	def isPalinSent(self, s):
		# code here
		new = ""
		for c in s:
		    if c.isalnum():
		        new+=c.lower()

		for i in range(len(new)//2):
		    if new[i]!=new[len(new)-i-1]:
		        return False
        return True