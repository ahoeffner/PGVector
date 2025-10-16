import requests

URL = "http://127.0.0.1:8000"


def health():
	url = f"{URL}/health"
	try:
		r = requests.get(url)

		# 1. Assert the status code is 200 (OK)
		assert r.status_code == 200

		# 2. Assert the JSON response content is correct
		response = r.json()
		assert response == {"status": "ok"}

		print(f"Health check successful!")
		print(f"Status Code: {r.status_code}")
		print(f"Response: {response}")

	except requests.exceptions.ConnectionError:
		print(f"ERROR: Failed to connect to {url}")
		return

	except AssertionError as e:
		print(f"Assertion failed: Received status code {r.status_code}")
		return


def index():
	url = f"{URL}/index"

	data = {"b64": "SGVsbG8gd29ybGQh"}  # Base64 for "Hello world!"

	try:
		r = requests.post(url, json=data)

		assert r.status_code == 200

		json = r.json()
		chunks = json.get("chunks", [])

		print(f"Index check successful!")
		print(f"Status Code: {r.status_code}")
		print(f"Response: {chunks[0]['embedding']}")

	except requests.exceptions.ConnectionError:
		print(f"ERROR: Failed to connect to {url}")
		return

	except AssertionError as e:
		print(f"Assertion failed: Received status code {r.status_code}")
		return


if __name__ == "__main__":
	 index()