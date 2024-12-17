import requests

# Endpoint IAM Token
url = "https://iam.cloud.ibm.com/identity/token"

# Header dan data
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
    "apikey": "IZpyluA4pt0WmXLAQVY2u_eSnvhY1PD2bYqufTAAWMXb"
}

# Kirim permintaan POST
response = requests.post(url, headers=headers, data=data)

# Periksa respons
if response.status_code == 200:
    print("Access Token:", response.json()["access_token"])
else:
    print("Error:", response.status_code, response.text)
