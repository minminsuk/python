# Using for loop
odd_sum_for = 0
for i in range(1, 101):
    if i % 2 != 0:
        odd_sum_for += i
print("1에서 100까지의 홀수의 합:", odd_sum_for)

# Using while loop
odd_sum_while = 0
i = 1
while i <= 100:
    if i % 2 != 0:
        odd_sum_while += i
    i += 1
print("1에서 100까지의 홀수의 합:", odd_sum_while)