import requests

url = "https://moodleprod.murdoch.edu.au/mod/resource/view.php?id=2678132"
response = requests.get(url, allow_redirects=True, stream=True)

# Check final URL after redirects
print("Final URL:", response.url)

# Check if it's a downloadable file
content_disp = response.headers.get("Content-Disposition")
content_type = response.headers.get("Content-Type")

print("Content-Disposition:", content_disp)
print("Content-Type:", content_type)
