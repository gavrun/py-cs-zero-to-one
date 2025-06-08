# 07_python_advanced/regular_expressions_intro.py

# Regular Expressions in Python

# Using the built-in 're' module

import re


# 1. Basic Matching: re.match vs re.search vs re.fullmatch

text = "Error: file not found"

# re.match checks only the beginning of the string
if re.match(r"Error", text):
    print("Matched using re.match")

# re.search scans the entire string
if re.search(r"file", text):
    print("Matched using re.search")

# re.fullmatch matches the whole string
if re.fullmatch(r"Error: file not found", text):
    print("Matched using re.fullmatch")


# 2. Character Classes, Quantifiers, Anchors

sample = "abc123XYZ"

# Character classes and quantifiers
pattern = r"[a-z]+[0-9]+[A-Z]+"
if re.fullmatch(pattern, sample):
    print("Pattern with character classes matched")

# Anchors: ^ = start, $ = end
if re.match(r"^abc", sample) and re.search(r"XYZ$", sample):
    print("Anchors used to match start and end")


# 3. Groups and Capturing

email = "john.doe@example.com"

match = re.search(r"([\w\.]+)@([\w\.]+)", email)
if match:
    username = match.group(1)
    domain = match.group(2)
    print("User:", username)
    print("Domain:", domain)


# 4. Named Groups

date = "2025-06-07"
match = re.match(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", date)
if match:
    print("Year:", match.group("year"))
    print("Month:", match.group("month"))
    print("Day:", match.group("day"))


# 5. Substitution with re.sub

text = "The price is $45.00"
new_text = re.sub(r"\$\d+(\.\d{2})?", "[REDACTED]", text)
print("After substitution:", new_text)

# Using a function in re.sub
def censor(match):
    return match.group(1)[0] + "***"

censored = re.sub(r"\b(\w+)\b", censor, "bad word example")
print("Censored text:", censored)


# 6. Flags: IGNORECASE, MULTILINE, DOTALL

multiline_text = "Line 1\nLine 2\nline 3"

# re.IGNORECASE (i), re.MULTILINE (m), re.DOTALL (s)
matches = re.findall(r"^line", multiline_text, re.IGNORECASE | re.MULTILINE)
print("Lines starting with 'line' (case-insensitive):", matches)

# DOTALL allows '.' to match newlines
match = re.search(r"Line.*3", multiline_text, re.DOTALL)
if match:
    print("DOTALL matched:", match.group())


# 7. Lookahead and Lookbehind

passwords = ["abc123", "abc", "123abc", "abc123!"]

# Positive lookahead: must contain at least one digit
for p in passwords:
    if re.fullmatch(r"(?=.*\d).+", p):
        print("Password with digit:", p)

# Negative lookbehind: must not be preceded by 'not'
text = "I am happy. I am not sad."
matches = re.findall(r"(?<!not )\bsad\b", text)
print("Found not-negated 'sad':", matches)


# 8. Compiling patterns

phone_pattern = re.compile(r"\(\d{3}\) \d{3}-\d{4}")

phones = ["(123) 456-7890", "123-456-7890"]
for phone in phones:
    if phone_pattern.fullmatch(phone):
        print("Valid phone number:", phone)


# 9. Useful utilities: re.split and re.findall

text = "one, two; three|four"
parts = re.split(r"[,\|;] ?", text)
print("Split parts:", parts)

numbers = re.findall(r"\d+", "abc 123 def 456")
print("All numbers:", numbers)

