numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
prime_count = 0
composite_count = 0
for num in numbers:
    if num < 2:
        continue  
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        prime_count += 1
    else:
        composite_count += 1

print("Prime count:", prime_count)
print("Composite count:", composite_count)
