import requests

def ssti_scan(url):
    vulnerabilities = []
    log_text = ""

    try:
        response = requests.get(url)
        if "name" in response.text:
            payloads = [
                "{{ 7*7 }}",
                "${{ 7*7 }}",
                "#{ 7*7 }",
                "${ 7*7 }",
                "{{ self.__class__.__base__.__subclasses__() }}",
                "${{ self.__class__.__base__.__subclasses__() }}",
                "#{ self.__class__.__base__.__subclasses__() }",
                "${ self.__class__.__base__.__subclasses__() }",
            ]
            
            for payload in payloads:
                payload_url = f"{url}?name={payload}"
                response = requests.get(payload_url)
                log_text += f"Payload: {payload}, URL: {payload_url}, Status: "
                if payload in response.text:
                    vulnerabilities.append((payload, url, "Pass"))
                    log_text += "Pass\n"
                else:
                    log_text += "Fail\n"

    except Exception as e:
        print(f"Error scanning {url}: {e}")

    # Write log text to file
    log_file = f"{url.split('//')[1]}_ssti_log.txt"
    with open(log_file, "w") as f:
        f.write(log_text)

    return vulnerabilities
