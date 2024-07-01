import pyshorteners

""" [ pip Install pyshorteners ]"""

url = input("Enter URL for shortening : \n")

print("URL After Shortening :- ", pyshorteners.Shortener().tinyurl.short(url))
