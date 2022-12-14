import urllib.request, urllib.error, urllib.parse
url = input("Enter Your Url Here With http://-")

fhand = urllib.request.urlopen(url)
counts = dict()
for line in fhand :
  words = line.decode().strip()
  print(words)
  for word in words :
    counts[word] = counts.get(word, 0) +1
print(counts)
