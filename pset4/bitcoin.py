import sys
import requests


def main():
    dollar = obtaining_value()

    # Authorization of the API
    api_key = "0227f3ba63b60a2266e0640843cd028fab9513f94cc4422b06f3ba10e114fb76"
    amount = request_api(dollar=dollar, api_key=api_key)
    print(f"${amount:,.4f}")


def obtaining_value():

    # Review if there is an argument when running the code
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    else:
        try:
            dollar = float(sys.argv[1])
        except:
            sys.exit("Command-line argument is not a number")
    return dollar


def request_api(dollar: int, api_key: str):
    try:
        headers = {"Authorization": f"Bearer {api_key}"}
        """
        request = requests.get(
            "https://rest.coincap.io/v3/assets?search=bitcoin", headers=headers
        )
        """
        request = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=" + api_key
        )
        bitcoin_dict = request.json()["data"]["priceUsd"]  # dictionary of bitcoin
        bitcoin_value = float(bitcoin_dict)
        return bitcoin_value * dollar
    except:
        sys.exit("No possible communication")


if __name__ == "__main__":
    main()
