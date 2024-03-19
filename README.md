# WarpOnWarp Generator

This Python program, named "WarpOnWarp Generator" facilitates the generation of WarpOnWarp configurations using an API provided by "zeroteam.top." WarpOnWarp is a service that enables users to access the free world internet securely through a singbox/hiddify configuration.

## Features

- Generates WarpOnWarp configurations using the API from "zeroteam.top."
- Allows customization of clean IP addresses for enhanced privacy.
- Saves the generated configurations in the `/output` directory.

## Prerequisites

- Python 3.x
- Requests library (Install using `pip install requests`) or:


## Usage

1. Clone the repository to your local machine.
```bash
git clone https://github.com/drunkleen/warp-on-warp-generator
```
2. Install the necessary dependencies (`requests` library).
```bash
pip install -r requirements.txt
```
3. Run the `warp-on-warp-generator.py` script.
```bash
python warp-on-warp-generator.py
```
4. Follow the prompts to customize the configuration, if desired.
5. Configurations will be saved in the `/output` directory.

## How It Works

1. The program loads a JSON template (`config-template.json`) which serves as the basis for the WarpOnWarp configuration.
2. It registers two Warp accounts using the API from "zeroteam.top."
3. The program then populates the JSON template with the obtained account details.
4. Optionally, the user can choose to use custom clean IP addresses for added privacy.
5. Finally, the modified JSON configuration is saved in the `/output` directory with a randomly generated filename.

## Configuration Customization

- The program prompts the user if they want to use a custom clean IP address. If selected, the user can input the IP address and port.
- If custom clean IP is not selected, default IP addresses and ports are used.

## Files

- `warp-on-warp-generator.py`: The Python script for generating WarpOnWarp configurations.
- `config-template.json`: Template JSON file for the WarpOnWarp configuration.
- `/output`: Directory to store the generated configurations.

## Disclaimer

- This program is provided as-is, without any warranties. Use it at your own risk.
- Ensure compliance with applicable laws and terms of service when using the generated configurations.

## Credits

- This program utilizes the API provided by "zeroteam.top" for WarpOnWarp configuration generation.

## License

- This project is licensed under the [MIT License](LICENSE).

For any issues or suggestions, feel free to open an issue or submit a pull request. Thank you for using the WarpOnWarp Generator!