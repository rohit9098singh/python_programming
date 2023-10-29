import re

pattern = "limited"
text = '''Flipkart rivate Limited is an Indian e-commerce company,
headquartered in Bangalore, and incorporated in Singapore as a
private limited company. The company initially focused on online
book sales before expanding into other product categories such as 
consumer electronics, fashion, home essentials, groceries, and lifestyle products.
The service competes primarily with Amazon India and domestic rival Snapdeal.
[5][6] As of March 2017, Flipkart held a 39.5% market share in the Indian e-commerce
industry.[7] Flipkart has a dominant position in the apparel segment, bolstered by its
acquisition of Myntra, and was described as being "neck and neck" with Amazon in the sale of electronics and mobile phones.'''
new_pattern = r"[A-Z]+ompany"

match = re.search(pattern, text)

if match:
    print("Pattern found at index:", match.start())
else:
    print("Pattern not found.")

matches = re.finditer(new_pattern, text)

print("Matches found for the new pattern:")
for match in matches:
    print("Found:", match.span())
