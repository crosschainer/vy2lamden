import argparse

def convert(input_file, output_file):
    vyper_file = open(input_file, "r")
    vyper_contract = vyper_file.read()
    vyper_contract = vyper_contract.splitlines()

    converted_contract = []
    #strip comments, imports (obv they are not on chain), interfaces (dont exist), events (dont exist)
    for line in vyper_contract:
        if not line.lstrip().startswith("#") and not line.lstrip().startswith("from") and "implements" not in line and "event" not in line and "@constant" not in line and "log." not in line:
            if "@public" in line:
                converted_contract.append("@export")
            else:
                converted_contract.append(line)

    for index, line in enumerate(converted_contract):
        if "__init__" in line:
            converted_contract[index-1] = "@construct"
            converted_contract[index] = converted_contract[index].replace("__init__", "seed")

    
    
    converted_contract = filter(None, converted_contract)
    converted_contract = '\n'.join(converted_contract)

    converted_file = open(output_file, "a")
    converted_file.write(converted_contract)
    converted_file.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', help='Vyper Input File Name')
    parser.add_argument('--output_file', help='Lamden Python Output File Name')
    args = parser.parse_args()
    convert(args.input_file, args.output_file)