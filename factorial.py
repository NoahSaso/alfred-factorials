# Initial code to create list
print('<?xml version="1.0"?>')
print('<items>')
print('<item uid="factorial" valid="no">')

# Get arguments
num = int("{query}")
result = 1

if num < 0:
	print('<title>Are you crazy? No negative numbers!</title>')
elif num == 0:
	print('<title>0! = 1 (still debated but this works)</title>')
else:
	# Loop through numbers and multiply to get factorial
	for i in range(1, num + 1):
		result = result * i
	# If result is bigger than 1 quintillion, put in scientific notation
	# Also create subtitle of full number
	if result > 1000000000000000000:
		# This formatting trick adds commas so it's more human readable
		print('<subtitle>'+"{:,}".format(result)+'</subtitle>')
		# This gives it scientific notation
		result = '%.2E' % result
	# If result is not bigger than 1 quintillion, print normally
	else:
		# This formatting trick adds commas so it's more human readable
		result = "{:,}".format(result)
	# Print our factorial'd number!
	print('<title>'+str(num)+'! = '+result+'</title>')

# Finish printing rest of code to show up
print('</item>')
print('</items>')
