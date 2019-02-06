import re

# Lesson 1
r"abc"

# Lesson 1.5
r"123"

# Lesson 2
r"\."

# Lesson 3
r"[cmf]an"

# Lesson 4
r"[hd]og"
r"[^b]og"

# Lesson 5
r"[ABC][nop][abc]"

# Lesson 6
r"waz{3}"
r"waz{3,5}"

# Lesson 7
r"a+b*c+"
r"aa+b*c+"
r"a{2,4}b{0,4}c{1,2}"

# Lesson 8
r"\d+ files* found\?"

# Lesson 9
r"\d+\.\s+abc"

# Lesson 10
r"^Mission:\ssuccessful$"

# Lesson 11
r"^(file\w+)\.pdf$"

# Lesson 12
r"[A-Z][a-z][a-z] \d{4}"
r"(\w+ (\d+))"

# Lesson 13
r"(\d{4})?x(\d{3,4})"
r"(\d+)x(\d+)"

# Lesson 14
r"^I love ([c]ats*|[d]ogs)"
r"I love (cats|dogs)"

# Lesson 15 LOL I still got it solved
r"(.*)"

# Challenge 1
r"\d{4}-\d{4}-\d{4}-\d{4}"
# Challenge 2
print("".join(re.split("[^a-zA-Z]*", "WA 7317 B")))
# Challenge 3
print("".join(re.split("[^0-9]*", "I wish I had 1 million dollars in all my 3 houses!")))

# Challenge 4
# Continue via https://school.nextacademy.com/courses/full-stack-web-development-bootcamp-with-python/lessons/2933