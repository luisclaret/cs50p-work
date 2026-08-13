import re
import sys

def main():
    print(parse(input("HTML: ")))
    
def parse(str: str) -> str:
    pattern = r'<iframe[^>]*\ssrc="https?://(?:www\.)?youtube\.com/embed/([^"]+)"'
    match = re.search(pattern, str)
    if match:
        return "https://youtu.be/" + match.group(1)
    else:
        return None

if __name__ == "__main__":
    main()
