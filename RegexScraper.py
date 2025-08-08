import re
import sys 



"""
OSINT Recon Script (Skeleton)
Author: Habib "The Ghost Analyst"
Description:
    A basic OSINT reconnaissance script framework.
    Designed for educational and ethical purposes only.
"""

print("Enter text to search for phone numbers, emails and links (Press Ctrl+D when done): ")
fire = sys.stdin.read()

phones = re.findall(r"(?:\(?\+?\d{1,3}\)?\s?\-?)?(?:\(?\d{2,4}\)?[\s.-]?)?\d{3,4}[\s.-]?\d{4}", fire)
emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", fire, re.IGNORECASE)
links = links = re.findall(r'(https?://[^\s]+|\www\.[^\s]+)', fire)





print("\nPhone Matches:\n")
if not phones:
        print("No matches found for phone numbers.")
else:
    for match in phones:
        print(match)  
    print(f"{len(phones)} phone numbers were extracted.")
print('#################################\n')

print("Email Matches:\n")
if not emails:
        print("\nNo matches found for emails.")
else:
    for match in emails:
        print(match)
    print(f"{len(emails)} email address(es) were extracted.")
print('#################################\n')

print("Link Matches:\n")
if not links:
    print("\nNo matches found for links.")
else:
    for match in links:
        print(match)
    print(f"{len(links)} link(s) were extracted.")
print('#################################\n')


if not phones and not emails and not links:
    print("No matches found for phone numbers, emails, or links")




