'''
Accidental breaking of stuff
Adit
2023
'''

PODCAST ='Sorry About That'
TOPIC = ' Accidental breaking of stuff'
OFFENDER = 'Adit'
STARTING_YEAR =2023
total_offenses = 0
print(f'welcome to {PODCAST}, the podcast about {TOPIC}')
num_months = 12
month_counter = 0
starting_month = 4
num_years = 2

#For Loops
for year_counter in range(num_years):
    for month_counter in range(starting_month,num_months,2):
        offense_count = int(input(f'how many offenses in month {month_counter} of year {year_counter}?: '))
        total_offenses += offense_count
    print(f'Ended year {year_counter}')
print(f'{OFFENDER} commited {total_offenses} offenses in {num_years} years')

dna_sequence = "catagcatagatag"
a_count = 0
for character in dna_sequence:
    print(character)
    if character == 'a':
        a_count += 1
#While Loops
'''
while month_counter < num_months:
    offense_count = int(input(f'how many offenses in month {month_counter}?: '))
    total_offenses += offense_count
    month_counter += 1
print(f'{OFFENDER} commited {total_offenses} offenses in {month_counter} months')
'''
#While not done Loop
'''
done = False
while not done:
    offense_count = int(input(f'how many offenses in month {month_counter}?: '))
    if offense_count < 0:
        done = True
    else:
        total_offenses += offense_count
        month_counter += 1
print(f'{OFFENDER} commited {total_offenses} offenses in {month_counter} months')
'''