import requests

print("Usage example : python3 main.py" )
print("[+] file_path > /home/user/Desktop/file.txt")
print("[+] enter web path > /admin/filemanger/upload.php")
print("")
while True:
    file_name = input("file_path > ")
    new_path = input("enter web path > ")
    result_file_name = "result.txt"
    valid_urls = []

    with open(file_name, 'r+') as file:
        lines = file.readlines()

        for i in range(len(lines)):
            lines[i] = lines[i].strip() + new_path + '\n'

        file.seek(0)
        file.writelines(lines)
        file.truncate()

    with open(file_name, 'r') as file:
        for line in file:
            url = line.strip()
            print(url)

            try:
                response = requests.get(url)
                print(f"Status code: {response.status_code}")

                if response.status_code == 200:
                    valid_urls.append(url)
            except requests.RequestException as e:
                print(f"Error: {e}")

    with open(result_file_name, 'w') as result_file:
        for valid_url in valid_urls:
            result_file.write(valid_url + '\n')

    print(f"[+] The path {new_path} has been added to all websites in the file.")
    print(f"[+] URLs with status code 200 have been saved to {result_file_name}.")
