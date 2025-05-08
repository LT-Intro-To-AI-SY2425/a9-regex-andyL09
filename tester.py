import wikipedia
import re

lane_page = wikipedia.WikipediaPage("Lane Tech College Prep High School")
lane_page.content
print(lane_page.content)
print("----------------------------------------------------------------")

# Extract the first paragraph
first_paragraph = lane_page.content.split("\n\n")[0]
print(first_paragraph)
print("----------------------------------------------------------------")
# Extract all numbers in the article
allNumbers = lane_page.content.split("\d+")

#does not work???? figure it out later