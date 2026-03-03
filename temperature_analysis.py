# Name: Divya Sri
# Roll Number: iitp_aimltn_2602242
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]


maximum  = temperatures[0]
minimum = temperatures[0]

for temp in temperatures[1::]:
    if temp > maximum:
        maximum = temp
    elif temp < minimum:
        minimum = temp
        
print(f"Highest Temperature : {maximum}℃")
print(f"Lowest Temperature : {minimum}℃")


print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

count = 0
for temp in temperatures:
    if temp <= 30:
        continue
    else:
        count+=1
        
print(f"Temperatures more than 30℃ : {count} days")


print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]

count = 0
for index,temp in enumerate(temperatures):
    if temp >= 40:
        print(f"Hot days before alert: {count}")
        print(f"Alert! Extreme temperature 40 detected on day {index+1}")
        break
    elif temp > 30 and temp < 40:
        count += 1
    else:
        continue
