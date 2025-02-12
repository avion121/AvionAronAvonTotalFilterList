import requests
import datetime

# URLs of the filter lists
FILTER_LIST_URLS = {
    "Hagezi_Pro": "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/adblock/pro.txt",
    "StevenBlack_Fakenews_Gambling": "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling/hosts",
    "OISD_Big_List": "https://big.oisd.nl",
    "EasyList": "https://easylist.to/easylist/easylist.txt",
    "EasyPrivacy": "https://easylist.to/easylist/easyprivacy.txt",
    "1Hosts_Lite": "https://raw.githubusercontent.com/badmojr/1Hosts/master/Lite/adblock.txt"
}

# Output file
OUTPUT_FILE = "AvionAronAvonTotalFilterList.txt"

def download_filter_list(url):
    """Download a filter list from the given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return None

def compile_filter_lists():
    """Download and compile all filter lists into one."""
    compiled_list = []

    # Add a header to the compiled list
    compiled_list.append(f"! AvionAronAvonTotalFilterList\n")
    compiled_list.append(f"! Last Updated: {datetime.datetime.now()}\n")
    compiled_list.append(f"! Sources:\n")
    for name, url in FILTER_LIST_URLS.items():
        compiled_list.append(f"! - {name}: {url}\n")
    compiled_list.append("\n")

    # Download and append each filter list
    for name, url in FILTER_LIST_URLS.items():
        print(f"Downloading {name}...")
        filter_list = download_filter_list(url)
        if filter_list:
            compiled_list.append(f"! Start of {name}\n")
            compiled_list.append(filter_list)
            compiled_list.append(f"! End of {name}\n\n")
        else:
            print(f"Skipping {name} due to download error.")

    # Write the compiled list to a file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.writelines(compiled_list)
    print(f"Compiled filter list saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    compile_filter_lists()
