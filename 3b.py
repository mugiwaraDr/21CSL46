from difflib import SequenceMatcher

s1 = input("enter s1:")
s2 = input("enter s2:")
print("the similarity b/w ", s1, "and ", s2, "is", SequenceMatcher(None, s1, s2).ratio())
