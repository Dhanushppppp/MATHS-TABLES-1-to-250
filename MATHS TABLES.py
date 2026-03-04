# Print multiplication tables from 1 to 20

for num in range(1,251):
    print("f\nmultiplication tables of {num}")
    print("-" * 25)
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
