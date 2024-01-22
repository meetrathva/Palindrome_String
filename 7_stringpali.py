a = input("Enter String: ")
rev = a[::-1]
fh = open("7_stringpali.txt","w")
fh.write(str(a))
if (rev == a):
    fh.write("\nGiven string is palindrome.")
else:
    fh.write("\nGiven string is NOT palindrome.")
fh.close()