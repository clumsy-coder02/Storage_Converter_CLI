# math module
import math

# input values
print() # spacing 
print("Storage Converter")
print("Convert from one data(images, videos or files(documents or PDFs)) size to another")
print() # spacing

print("What format is your data;\n\nEnter 1 for:GB\nEnter 2 for:MB\nEnter 3 for:KB"
      "\nEnter 4 for:Byte\nEnter 5 for:Nibble\nEnter 6 for:Exit")
print() # spacing
choice = int(input("Select one option from the list above(1-6): "))

# main function
def option_selection():
    if choice == 1:
        GB_data_format()
    elif choice == 2:
        MB_data_format()
    elif choice == 3:
        KB_data_format()
    elif choice == 4:
        byte_data_format()
    elif choice == 5:
        nibble_data_format()
    elif choice == 6:
        exit_program()

# conversion functions
# data in GB format function
def GB_data_format():
    file_size_in_GB = float(input("Enter the size of the data: "))
    print() # spacing
    print(f"Would you like to convert from;\n\nEnter 1 for; GB to MB\nEnter 2 for; GB to KB\n"
        "Enter 3 for; GB to Bytes\nEnter 4 for; GB to Nibbles\nEnter 5 for; GB to Bits")
    print() # spacing

    second_choice = int(input("Select one option from the list above(1-5): "))
    if second_choice == 1:
        # straight conversion from GB to MB
        file_size_in_MB = file_size_in_GB * 1024
        # convert from GB to MB(decimal format)
        file_size_in_mb = file_size_in_GB * 1000

        print() # spacing
        result_decimal = f"Your data in MB(decimal format): readable; {math.trunc(int(file_size_in_mb)):,d} accurate; {file_size_in_mb} MegaBytes"
        result_binary = f"Your data in MB(binary format): readable; {math.trunc(int(file_size_in_MB)):,d} accurate; {file_size_in_MB} MegaBytes"
        results = f"{result_decimal}\n{result_binary}"
        print() # spacing

    elif second_choice == 2:
        # first convert from GB to MB then take that value & convert to KB
        file_size_in_KB = (file_size_in_GB * (1024**2))
        # convert from GB to KB(decimal format)
        file_size_in_kb = (file_size_in_GB * (1000**2))

        print() # spacing
        result_decimal = f"Your data in KB(decimal format): readable; {math.trunc(int(file_size_in_kb)):,d} accurate; {file_size_in_kb} KiloBytes"
        result_binary = f"Your data in KB(binary format): readable; {math.trunc(int(file_size_in_KB)):,d} accurate; {file_size_in_KB} KiloBytes"
        results = f"{result_decimal}\n{result_binary}"
        print() # spacing

    elif second_choice == 3:
        # exponentiation used for repeated multiplication
        # convert from GB to MB from MB to KB then finally from KB to bytes
        file_size_in_Bytes = (file_size_in_GB * (1024**3))
        # convert from GB to MB from MB to KB then from KB to bytes
        file_size_in_bytes = (file_size_in_GB * (1000**3))

        print() # spacing
        result_decimal = f"Your data in Bytes(decimal format): readable; {math.trunc(int(file_size_in_bytes)):,d} accurate; {file_size_in_bytes} Bytes"
        result_binary = f"Your data in Bytes(binary format): readable; {math.trunc(int(file_size_in_Bytes)):,d} accurate; {file_size_in_Bytes} Bytes"
        results = f"{result_decimal}\n{result_binary}"
        print() # spacing

    elif second_choice == 4:
        # convert from GB to bytes then from bytes to bits then finally from bits to nibbles
        file_size_in_nibbles = (file_size_in_GB * (1024**3) * 8) // 4
        # convert from GB to bytes then from bytes to bits then from bits to nibbles(decimal)
        file_size_in_Nibbles = (file_size_in_GB * (1000**3) * 8) // 4

        print() # spacing
        result_decimal = f"Your data in nibbles(decimal format): readable; {math.trunc(int(file_size_in_Nibbles)):,d} accurate; {file_size_in_Nibbles} Nibbles"
        result_binary = f"Your data in nibbles(binary format): readable; {math.trunc(int(file_size_in_nibbles)):,d} accurate; {file_size_in_nibbles} Nibbles"
        results = f"{result_decimal}\n{result_binary}"
        print() # spacing

    elif second_choice == 5:
        # convert from GB straight to bytes then from bytes to bits
        file_size_in_bits = (file_size_in_GB * (1024**3) * 8)
        # convert from GB straight to bytes then from bytes to bits(decimal)
        file_size_in_Bits = (file_size_in_GB * (1000**3) * 8)

        print() # spacing
        result_binary = f"Your data in bits(binary format): readable; {math.trunc(int(file_size_in_bits)):,d} accurate; {file_size_in_bits} Bits"
        result_decimal = f"Your data in bits(decimal format): readable; {math.trunc(int(file_size_in_Bits)):,d} accurate; {file_size_in_Bits} Bits"
        print() # spacing
    else:
        results = "Follow instructions and always select an option😁"

    return print(results)

# data in MB format function
def MB_data_format():
    file_size_in_MB = float(input("Enter the size of the data: "))
    print() # spacing
    print(f"Would you like to convert from;\n\nEnter 1 for; MB to KB\nEnter 2 for; MB to Bytes"
          "\nEnter 3 for; MB to Nibbles\nEnter 4 for; MB to Bits")
    print() # spacing

    second_choice = int(input("Select one option from the list above(1-4): "))
    if second_choice == 1:
        # straight conversion from MB to KB
        file_size_in_KB = file_size_in_MB * 1024
        print() # spacing
        results = f"Your data in KB(binary format): {file_size_in_KB} Kilobytes\nYour data in KB(readable format): {math.trunc(file_size_in_KB):,d} Kilobytes"
        print() # spacing
    elif second_choice == 2:
        # convert from MB to KB then from KB to bytes
        file_size_in_bytes = (file_size_in_MB * (1024**2))
        print() # spacing
        results = f"Your data in bytes(binary format): {file_size_in_bytes} Bytes\nYour data in bytes(readable format): {math.trunc(file_size_in_bytes):,d} Bytes"
        print() # spacing
    elif second_choice == 3:
        # convert straight from MB to bytes then from bytes to bits then finally from bits to nibbles
        file_size_in_nibbles = (file_size_in_MB * (1024**2) * 8) // 4
        print() # spacing
        results = f"Your data in nibbles(binary format): {file_size_in_nibbles} Nibbles\nYour data in nibbles(readable format): {math.trunc(file_size_in_nibbles):,d} Nibbles"
        print() # spacing
    elif second_choice == 4:
        # convert from MB to bytes then from bytes to bits
        file_size_in_bits = (file_size_in_MB * (1024**2) * 8)
        print() # spacing
        results = f"Your data in bits(binary format): {file_size_in_bits} Bits\nYour data in bits(readable format): {math.trunc(file_size_in_bits):,d} Bits"
        print() # spacing
    else:
        results = "Follow instructions and always select an option😁"

    return print(results)

# data in KB format function
def KB_data_format():
    file_size_in_KB = float(input("Enter the size of the data: "))
    print() # spacing
    print(f"Would you like to convert from;\n\nEnter 1 for; KB to Bytes\nEnter 2 for; KB to Nibbles"
          "\nEnter 3 for; KB to Bits")
    print() # spacing

    second_choice = int(input("Select one option from the list above(1-3): "))
    if second_choice == 1:
        # straight conversion from KB to bytes
        file_size_in_bytes = file_size_in_KB * 1024
        print() # spacing
        results = f"Your data in bytes(binary format): {file_size_in_bytes} Bytes\nYour data in bytes(readable format): {math.trunc(file_size_in_bytes):,d} Bytes"
        print() # spacing
    elif second_choice == 2:
        # convert from KB to bytes then from bytes to bits then finally from bits to nibbles
        file_size_in_nibbles = ((file_size_in_KB * 1024) * 8) // 4
        print() # spacing
        results = f"Your data in nibbles(binary format): {file_size_in_nibbles} Nibbles\nYour data in nibbles(readable format): {math.trunc(file_size_in_nibbles):,d} Nibbles"
        print() # spacing
    elif second_choice == 3:
        # convert from KB to bytes then from bytes to bits
        file_size_in_bits = ((file_size_in_KB * 1024) * 8)
        print() # spacing
        results = f"Your data in bits(binary format): {file_size_in_bits} Bits\nYour data in bits(readable format): {math.trunc(file_size_in_bits):,d} Bits"
        print() # spacing
    else:
        results = "Follow instructions and always select an option😁"

    return print(results)

# data in byte format function
def byte_data_format():
    file_size_in_bytes = float(input("Enter the size of the data: "))
    print() # spacing
    print(f"Would you like to convert from;\n\nEnter 1 for; Bytes to Nibbles\nEnter 2 for; Bytes to Bits")
    print() # spacing

    second_choice = int(input("Select one option from the list above(1-2): "))
    if second_choice == 1:
        # convert the bytes to bits then from bits to nibbles
        file_size_in_nibbles = (file_size_in_bytes * 8) // 4
        print() # spacing
        results = f"Your data in nibbles(binary format): {file_size_in_nibbles} Nibbles\nYour data in nibbles(readable format): {math.trunc(file_size_in_nibbles):,d} Nibbles"
        print() # spacing
    elif second_choice == 2:
        # convert straight from bytes to bits
        file_size_in_bits = file_size_in_bytes * 8
        print() # spacing
        results = f"Your data in bits(binary format): {file_size_in_bits} Bits\nYour data in bits(readable format): {math.trunc(file_size_in_bits):,d} Bits"
        print() # spacing
    else:
        results = "Follow instructions and always select an option😁"

    return print(results)

# data in nibble format function
def nibble_data_format():
    file_size_in_nibbles = float(input("Enter the size of the data: "))
    print() # spacing
    print(f"Would you like to convert from;\n\nEnter 1 for; Nibbles to Bits")
    print() # spacing

    second_choice = int(input("Select the option above('Press 1'): "))

    if choice == 1:
        # convert from nibbles to bits
        file_size_in_bits = file_size_in_nibbles * 4
        print() # spacing
        results = f"Your data in bits(binary format): {file_size_in_bits} Bits\nYour data in bits(readable format): {math.trunc(file_size_in_bits):,d} Bits"
        print() # spacing
    else:
        results = "Follow instructions and always select an option😁"
    
    return print(results)

# exit the program function
def exit_program():
    return exit()


if __name__ == "__main__":
    option_selection()