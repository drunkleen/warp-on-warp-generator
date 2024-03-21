import json
import os
import random
import string

import requests

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def generate_random_string() -> str:
    return "".join(random.choices(string.ascii_letters + string.digits, k=8))


def load_json_template() -> json:
    try:
        with open("config-template.json", "r") as file:
            data = json.load(file)
        return data
    except IOError:
        print("Error loading:\nconfig-template.json not found\n\n", IOError)


def check_output_dir():
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


def register_warp_account() -> json:
    try:
        return requests.get("https://api.zeroteam.top/warp?format=sing-box").json()
    except requests.exceptions.RequestException as e:
        print("Error registering")


if __name__ == "__main__":
    try:
        json_file_to_save = load_json_template()
        print(f"[+] {GREEN}Config Template loaded.{RESET}")
        first_account = register_warp_account()
        print(f"[+] {GREEN}First account registered.{RESET}")
        second_account = register_warp_account()
        print(f"[+] {GREEN}Second account registered.{RESET}")

        json_file_to_save["outbounds"][2]["local_address"][1] = first_account[
            "local_address"
        ][1]
        json_file_to_save["outbounds"][2]["private_key"] = first_account["private_key"]
        json_file_to_save["outbounds"][2]["reserved"] = first_account["reserved"]

        json_file_to_save["outbounds"][3]["local_address"][1] = second_account[
            "local_address"
        ][1]
        json_file_to_save["outbounds"][3]["private_key"] = second_account["private_key"]
        json_file_to_save["outbounds"][3]["reserved"] = second_account["reserved"]

        if (
            input(
                f"{YELLOW}[+] Do you want to use custom clean IP? (y/N): {RESET}"
            ).lower()
            == "y"
        ):
            ip = input("Enter clean IP address: ").strip()
            port = int(input("Enter clean the port of the clean IP: ").strip())

            json_file_to_save["outbounds"][3]["server"] = ip
            json_file_to_save["outbounds"][3]["server_port"] = port
            json_file_to_save["outbounds"][3]["server"] = ip
            json_file_to_save["outbounds"][3]["server_port"] = port
        else:
            json_file_to_save["outbounds"][2]["server"] = "162.159.193.10"
            json_file_to_save["outbounds"][2]["server_port"] = 2408
            json_file_to_save["outbounds"][3]["server"] = "162.159.193.10"
            json_file_to_save["outbounds"][3]["server_port"] = 2408

        check_output_dir()
        config_name = str(generate_random_string()) + ".json"
        with open(f"output/{config_name}", "w") as f:
            f.write(json.dumps(json_file_to_save))

        print(
            f"\n[+] {GREEN}Config was successfully created!{RESET}\n[+] {GREEN}Generated config saved:\n      {RESET}{os.getcwd()}/output/{config_name}\n"
        )

    except Exception as e:
        print(f"{RED}[+] Couldn't make the config.\nThere was an error:{RESET}\n{e}")
