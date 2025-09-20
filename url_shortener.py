import sys
import hashlib

urls = {}

def shorten_url(url):
    # Bug: Simple hash, collisions possible
    short_hash = hashlib.md5(url.encode()).hexdigest()[:6]
    urls[short_hash] = url
    return short_hash

def expand_url(code):
    return urls[code]  # Bug: crashes if code not in dict

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 url_shortener.py [shorten|expand] [URL|code]")
        return
    cmd = sys.argv[1]
    if cmd == "shorten":
        original_url = sys.argv[2]
        code = shorten_url(original_url)
        print(f"Shortened URL code: {code}")
    elif cmd == "expand":
        code = sys.argv[2]
        print(f"Original URL: {expand_url(code)}")
    else:
        print("Unknown command.")

if __name__ == "__main__":
    main()
