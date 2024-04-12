import requests
import re

def test_scores_service(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Extract score using regex
            score_match = re.search(r'The current score is: (\d+)', response.text)
            if score_match:
                score = int(score_match.group(1))
                if 1 <= score <= 1000:
                    print("Web service is working fine. Score is within the range.")
                    return True
                else:
                    print("Web service is working, but score is not within the range.")
                    return False
            else:
                print("Failed to find score element in the web page.")
                return False
        else:
            print(f"Failed to access web service. Status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def main_function():
    url = "http://127.0.0.1:5000"
    if not test_scores_service(url):
        return -1
    return 0

if __name__ == "__main__":
    exit_code = main_function()
    exit(exit_code)
