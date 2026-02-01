import random

# ANSI color codes
RESET = "\033[0m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
RED = "\033[31m"
BLUE = "\033[34m"
GREEN = "\033[32m"

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
temperature_values = []

for i in range(7):
    random_temperature = random.randint(1, 35)
    temperature_values.append(random_temperature)

print(CYAN + "\n========== WEEKLY TEMPERATURE REPORT ==========\n" + RESET)

for day, temperature in zip(days, temperature_values):
    print(f"{YELLOW}{day:<10} : {temperature:>3} °C{RESET}")

temperature_total = 0
for value in temperature_values:
    temperature_total += value

average_temperature = temperature_total / len(temperature_values)

print(BLUE + "\n----------------------------------------------" + RESET)
print(f"{GREEN}Weekly average temperature : {average_temperature:>6.2f} °C{RESET}")
print(BLUE + "----------------------------------------------" + RESET)

hottest = temperature_values[0]
hottest_day = days[0]

for temperature, day in zip(temperature_values, days):
    if temperature > hottest:
        hottest = temperature
        hottest_day = day

coldest = temperature_values[0]
coldest_day = days[0]

for temperature, day in zip(temperature_values, days):
    if temperature < coldest:
        coldest = temperature
        coldest_day = day

print(f"{RED}Hottest day of the week    : {hottest_day:<10} ({hottest:>2} °C){RESET}")
print(f"{BLUE}Coldest day of the week   : {coldest_day:<10} ({coldest:>2} °C){RESET}")

print(CYAN + "\n==============================================\n" + RESET)





