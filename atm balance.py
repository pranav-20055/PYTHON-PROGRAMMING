total_balance = 0

for i in range(4):
    denomination = int(input(f"Enter the {i+1}st Denomination: "))
    num_of_notes = int(input(f"Enter the {i+1}st Denomination number of notes: "))
    total_balance += denomination * num_of_notes

print("Total Available Balance in ATM:", total_balance)
