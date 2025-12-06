import requests
import os


url_extract = "https://raw.githubusercontent.com/biopython/biopython/master/Doc/examples/ls_orchid.fasta"


def extract_data(url=url_extract):
    response = requests.get(url)
    response.raise_for_status()  # Ensure we got a successful response
    return response.text

# converter dados extraidos da url em txt
def save_to_txt(data, filename="raw_data.txt"):
    with open(filename, "w") as file:
        file.write(data)

if __name__ == "__main__":
    data = extract_data()
    save_to_txt(data)
   
