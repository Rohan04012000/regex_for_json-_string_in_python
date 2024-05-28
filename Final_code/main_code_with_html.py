import re

#open HTML file as html_file and read the entire content into html_content.
with open('/index.html', 'r') as html_file:
  html_content = html_file.read()

#writing the regex expression to find the numbers with background colour set to orange.
pattern = re.compile(r'<span class="number">(\d+)</span>')

#Checking the type of html_content, which is string now, now it is easy to run regex,
print("file_content = ",type(html_content))

#finding all numbers using regex.
matches = re.findall(pattern, html_content)
#printing the numbers and the type of list, which stores thoese numbers.
print("matches = ",matches)
print("type of matches = ",type(matches))



