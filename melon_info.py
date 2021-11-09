"""Print out all the melons in our inventory."""
from melons import melon_details


def print_melons(melons):
    """Print each melon with corresponding attribute information."""

    for melon_name, attributes in melons.items():
        print(melon_name.upper())

        for attribute, value in attributes.items():
            print(f'{attribute}: {value}')

        print('===================================')

print_melons(melon_details)