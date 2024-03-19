palindrom = lambda s: s.lower().replace(" ","") == s[::-1].lower().replace(" ","")
print(palindrom("A man a plan a canal Panama"))