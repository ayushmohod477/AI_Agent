with open('data.txt', 'r') as file:
    data = file.readlines()

task = input("Are you an existing customer(yes/no): ")

match task:
    case "yes":
        customer_id = int(input('please Enter your customer id: '))
        try:
            cust_data = data[customer_id].split(",")
            pin = int(input("Enter your pin: "))
            if int(cust_data[2]) == pin:
                action = input("withdraw, deposit or transfer: ")
                match action:
                    case "withdraw":
                        amount = int(input("Enter the  amount to withdraw: "))
                        if amount < int(cust_data[0]):
                            cust_data[0] = str(int(cust_data[0]) - amount)
                            data[customer_id] = ','.join(cust_data) + '\n'
                            with open('data.txt', 'w') as file:
                                file.writelines(data)
                        else:
                            print("insufficient balance")
                    case "deposit":
                        amount = int(input("Enter the  amount to deposit: "))
                        cust_data[0] = str(int(cust_data[0]) + amount)
                        data[customer_id] = ','.join(cust_data) + '\n'
                        with open('data.txt', 'w') as file:
                            file.writelines(data)
                    case "transfer":
                        receiver_id = int(input("enter receivers id: "))
                        amount = int(input("Enter the  amount to transfer: "))
                        cust_data1 = data[receiver_id].split(",")
                        if amount < int(cust_data[0]):
                            cust_data1[0] = str(int(cust_data1[0]) + amount)
                            cust_data[0] = str(int(cust_data[0]) - amount)
                            data[customer_id] = ','.join(cust_data) + '\n'
                            data[receiver_id] = ','.join(cust_data1) + '\n'
                            with open('data.txt', 'w') as file:
                                file.writelines(data)
                        else:
                            print("insufficient balance")
            else:
                print("wrong pin")
        except IndexError:
            print("invalid customer id")
    case "no":
        detail = []
        email = input("Enter your Email")
        pin = input("gent=rate your pin: ")
        balance = input("Enter the amount to deposit: ")
        detail.append(balance)
        detail.append(email)
        detail.append(pin)
        detail = ",".join(detail) + '\n'
        data.append(detail)
        cust_id = len(data) - 1
        print(f"your customer id is {cust_id} please keep it safe")
        with open('data.txt', 'w') as file:
            file.writelines(data)
