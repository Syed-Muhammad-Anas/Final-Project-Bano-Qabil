amount_to_convert = input('Enter the amount you want to convert: ')
try:
    amount_to_convert = int(amount_to_convert)
    currency_to_convert_to = input("Enter the currency you want to convert from or type 'help' for help or type 'exit' to exit: ")
    while currency_to_convert_to.lower() != 'exit':
        if currency_to_convert_to == 'help':
            print("Enter the name of the currency you want to convert to from the following list: \n *USD \n *GBP \n *EUR \n *TRY \n *SAR \n *IRR \n *CNY \n ")
            currency_to_convert_to = input("Enter the name of the currency you want to convert to or type 'exit' to exit or type 'help' for help: ")
            if currency_to_convert_to.lower() == 'help':
                print("Help already displayed. Please choose from the above mentioned list. ")
                currency_to_convert_to = input("Enter the name of the currency you want to convert to or type 'exit' to exit: ")
        elif currency_to_convert_to.lower() == 'usd':
            rate_in_pkr = input('Specify the rate in PKR: ')
            amount_in_pkr = float(amount_to_convert) * float(rate_in_pkr)
            print(f"Amount in PKR is: {amount_in_pkr}")
            amount_to_convert = input('Enter the amount you want to convert: ')
            currency_to_convert_to = input("Enter the name of the currency you want to convert to or type 'exit' to exit or type 'help' for help: ")
        elif currency_to_convert_to.lower() == 'gbp':
            rate_in_pkr = input('Specify the rate in PKR: ')
            amount_in_pkr = float(amount_to_convert) * float(rate_in_pkr)
            print(f"Amount in PKR is: {amount_in_pkr}")
            amount_to_convert = input('Enter the amount you want to convert: ')
            currency_to_convert_to = input("Enter the name of the currency you want to convert to or type 'exit' to exit or type 'help' for help: ")
        elif currency_to_convert_to.lower() == 'eur':
            rate_in_pkr = input('Specify the rate in PKR: ')
            amount_in_pkr = float(amount_to_convert) * float(rate_in_pkr)
            print(f"Amount in PKR is: {amount_in_pkr}")
            amount_to_convert = input('Enter the amount you want to convert: ')
            currency_to_convert_to = input("Enter the name of the currency you want to convert to or type 'exit' to exit or type 'help' for help: ")
        elif currency_to_convert_to.lower() == 'try':
            rate_in_pkr = input('Specify the rate in PKR: ')
            amount_in_pkr = float(amount_to_convert) * float(rate_in_pkr)
            print(f"Amount in PKR is: {amount_in_pkr}")
            amount_to_convert = input('Enter the amount you want to convert: ')
            currency_to_convert_to = input("Enter the name of the currency you want to convert to or type 'exit' to exit or type 'help' for help: ")
        elif currency_to_convert_to.lower() == 'sar':
            rate_in_pkr = input('Specify the rate in PKR: ')
            amount_in_pkr = float(amount_to_convert) * float(rate_in_pkr)
            print(f"Amount in PKR is: {amount_in_pkr}")
            amount_to_convert = input('Enter the amount you want to convert: ')
            currency_to_convert_to = input("Enter the name of the currency you want to convert to or type 'exit' to exit or type 'help' for help: ")
        elif currency_to_convert_to.lower() == 'irr':
            rate_in_pkr = input('Specify the rate in PKR: ')
            amount_in_pkr = float(amount_to_convert) * float(rate_in_pkr)
            print(f"Amount in PKR is: {amount_in_pkr}")
            amount_to_convert = input('Enter the amount you want to convert: ')
            currency_to_convert_to = input("Enter the name of the currency you want to convert to or type 'exit' to exit or type 'help' for help: ")
        elif currency_to_convert_to.lower() == 'cny':
            rate_in_pkr = input('Specify the rate in PKR: ')
            amount_in_pkr = float(amount_to_convert) * float(rate_in_pkr)
            print(f"Amount in PKR is: {amount_in_pkr}")
            amount_to_convert = input('Enter the amount you want to convert: ')
            currency_to_convert_to = input("Enter the name of the currency you want to convert to or type 'exit' to exit or type 'help' for help: ")
        elif currency_to_convert_to.lower() == 'exit':
            break
        else:
            print("Sorry! the currency you have entered is not supported. Please try again.")
            currency_to_convert_to = input("Enter the name of the currency you want to convert to or type 'exit' to exit or type 'help' for help: ")
    print('Goodbye!😊👋')
except ValueError:
    print("Sorry! you have provided the program with an invalid input. Please run the program again and provide a numberical value.")