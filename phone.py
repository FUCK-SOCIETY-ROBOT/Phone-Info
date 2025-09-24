from os import system
from time import sleep
from colorama import Fore
from phonenumbers import geocoder, carrier, timezone, NumberParseException, PhoneNumberType
import phonenumbers

print("")
sleep(1)
system("clear" or "cls")
print("")

banr = Fore.LIGHTGREEN_EX+"""


⢀⣤⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣤⡀
⢸⣿⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣿⣿⡇
⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇
⢸⣿⣿⠀⠀⠀⠀⠀⣠⣦⡀⠀⠀⢀⣿⡟⠀⢀⣴⣄⠀⠀⠀⠀⠀⣿⣿⡇
⢸⣿⣿⠀⠀⠀⣠⣾⡿⠋⠀⠀⠀⢸⣿⠇⠀⠀⠙⢿⣷⣄⠀⠀⠀⣿⣿⡇
⢸⣿⣿⠀⠀⠘⢿⣿⣄⠀⠀⠀⢀⣿⡟⠀⠀⠀⠀⣠⣿⡿⠃⠀⠀⣿⣿⡇
⢸⣿⣿⠀⠀⠀⠀⠙⢿⣷⠄⠀⢸⣿⠇⠀⠀⠠⣾⡿⠋⠀⠀⠀⠀⣿⣿⡇
⢸⣿⣿⠀⠀⠀⠀⠀⠀⠁⠀⠀⠿⠟⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⣿⣿⡇
⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇
⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇
⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⢹⣿⣿⣿⣿⡏⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣼⣿⣿⣿⣿⣧⣤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
print(banr)

def get_full_phone_info(number: str, region: str = None) -> dict:
    try:
        parsed = phonenumbers.parse(number, region)
    except NumberParseException as e:
        return {"error": f"Invalid number: {e}"}

    info = {}
    info["is_valid"] = phonenumbers.is_valid_number(parsed)
    info["is_possible"] = phonenumbers.is_possible_number(parsed)

    info["E164"] = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
    info["INTERNATIONAL"] = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    info["NATIONAL"] = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)
    info["RFC3966"] = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.RFC3966)

    type_map = {
        PhoneNumberType.FIXED_LINE: "Fixed line",
        PhoneNumberType.MOBILE: "Mobile",
        PhoneNumberType.FIXED_LINE_OR_MOBILE: "Fixed line or Mobile",
        PhoneNumberType.TOLL_FREE: "Toll free",
        PhoneNumberType.PREMIUM_RATE: "Premium rate",
        PhoneNumberType.SHARED_COST: "Shared cost",
        PhoneNumberType.VOIP: "VOIP",
        PhoneNumberType.PERSONAL_NUMBER: "Personal number",
        PhoneNumberType.PAGER: "Pager",
        PhoneNumberType.UAN: "UAN",
        PhoneNumberType.VOICEMAIL: "Voicemail",
        PhoneNumberType.UNKNOWN: "Unknown"
    }
    info["type"] = type_map.get(phonenumbers.number_type(parsed), "Unknown")

    info["country_code"] = parsed.country_code
    info["country"] = geocoder.region_code_for_number(parsed)
    info["location"] = geocoder.description_for_number(parsed, "en")

    info["carrier"] = carrier.name_for_number(parsed, "en")

    info["timezone"] = timezone.time_zones_for_number(parsed)

    return info

if __name__ == "__main__":
    number = input(Fore.LIGHTYELLOW_EX+"Enter phone number (with country code, e.g. +989123456789): "+Fore.LIGHTGREEN_EX)
    print("")
    sleep(2)
    data = get_full_phone_info(number)
    for key, value in data.items():
        print(Fore.LIGHTCYAN_EX+f"{key}: {value}")