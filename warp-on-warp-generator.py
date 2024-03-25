import json
import os
import random
import string
import requests

# Define colors for better output formatting
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def generate_random_string(length=8) -> str:
    """Generate a random string of specified length."""
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


def load_json_template() -> dict:
    """Load the JSON template from the config-template.json file."""
    try:
        with open("config-template.json", "r") as file:
            data = json.load(file)
        return data
    except IOError as e:
        print(f"{RED}Error loading: config-template.json not found{RESET}\n{e}")
        raise


def check_output_dir():
    """Create the output directory if it doesn't exist."""
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)


def register_warp_account() -> dict:
    """Register a new Warp account."""
    try:
        response = requests.get("https://api.zeroteam.top/warp?format=sing-box").json()
        return response
    except requests.exceptions.RequestException as e:
        print(f"{RED}Error registering account{RESET}\n{e}")
        raise


def main():
    try:
        # Load the JSON template
        json_file_to_save = load_json_template()
        print(f"{GREEN}Config Template loaded.{RESET}")

        # Register two Warp accounts
        first_account = register_warp_account()
        print(f"{GREEN}First account registered.{RESET}")
        second_account = register_warp_account()
        print(f"{GREEN}Second account registered.{RESET}")

        # Update the JSON template with the registered accounts
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

        # Ask for custom clean IP and port
        use_custom_ip = (
            input(
                f"{YELLOW}[+] Do you want to use a custom clean IP? (y/N): {RESET}"
            ).lower()
            == "y"
        )
        if use_custom_ip:
            ip = input("Enter clean IP address: ").strip()
            port = int(input("Enter clean port: ").strip())
            json_file_to_save["outbounds"][2]["server"] = ip
            json_file_to_save["outbounds"][2]["server_port"] = port
            json_file_to_save["outbounds"][3]["server"] = ip
            json_file_to_save["outbounds"][3]["server_port"] = port
        else:
            json_file_to_save["outbounds"][2]["server"] = "162.159.193.10"
            json_file_to_save["outbounds"][2]["server_port"] = 2408
            json_file_to_save["outbounds"][3]["server"] = "162.159.193.10"
            json_file_to_save["outbounds"][3]["server_port"] = 2408

        # Create the output directory
        check_output_dir()

        # Save the configuration to a file
        config_name = f"{generate_random_string()}.json"
        config_path = os.path.join("output", config_name)
        with open(config_path, "w") as f:
            json.dump(json_file_to_save, f, indent=2)

        print(
            f"\n{GREEN}Config was successfully created!{RESET}\n{GREEN}Generated config saved:\n {RESET}{config_path}\n"
        )

    except Exception as e:
        print(f"{RED}[+] Couldn't make the config.\nThere was an error:{RESET}\n{e}")


if __name__ == "__main__":
    main()
