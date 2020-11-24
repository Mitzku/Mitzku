# create the initial variables below
age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0


# Add insurance estimate formula below
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

print("This person's insurance cost is " + str(insurance_cost) + " dollars.")

# Age Factor
age += 4

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated insurance cost after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars")

# BMI Factor
age =28

bmi += 3.1

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated insurance cost after increasing BMI by 3.1 by 4 years is " + str(change_in_insurance_cost) + " dollars")

# Male vs. Female Factor
bmi = 26.2
sex = 1

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated insurance cost for being male instead of female is " + str(change_in_insurance_cost) + " dollars")


# Write your first_three_multiples function here
def first_three_multiples(num):
  print(num*1)
  print(num*2)
  print(num*3)
  return print(num*3)

# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0





# Write your tip function here:
def tip(total, percentage):
  return (percentage/100) * total

# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0



# Write your introduction function here:
def introduction(first_name, last_name):
  return last_name, first_name, last_name

# Uncomment these function calls to test your introduction function:
print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou



# Create calculate_insurance_cost() function below:
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print("The estimated insurance cost for " + name +" is " + str(estimated_cost) + " dollars.")
  return estimated_cost

# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost("Maria", 28, 0, 26.2, 3, 0)



# Estimate Omar's insurance cost
omar_insurance_cost = calculate_insurance_cost("Omar", 35, 1, 22.2, 0, 1)




# Write your large_power function here:
def large_power(base, exponent):
  if base ** exponent > 5000:
    return True
  else:
    return False

# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False

# Write your over_budget function here:
def over_budget(budget, food_bill, electricity_bill, internat_bill, rent):
  if budget < (food_bill + electricity_bill + internat_bill + rent):
    return True
  else:
    return False

# Uncomment these function calls to test your over_budget function:
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True


# Write your in_range function here:
def in_range(num, lower, upper):
  if(num >= lower and num <= upper):
    return True
  return False

# Uncomment these function calls to test your in_range function:
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False


# Add your code here
def analyze_smoker(smoker_status):
  if smoker_status == 1:
    print("To lower your cost, you should consider quitting smoking.")
  else:
    print("Smoking is not an issue for you.")


def analyze_bmi(bmi_value):
  if bmi_value > 30:
    print("Your BMI is in the obese range. To lower your cost, you should significantly lower your BMI.")
  elif (bmi_value >= 25 and bmi_value <= 30):
    print("Your BMI is in the overweight range. To lower your cost, you should lower your BMI.")
  elif (bmi_value >= 18.5 and bmi_value <= 25):
    print("Your BMI is in a healthy range.")
  else:
    print(
      "Your BMI is in the underweight range. Increasing your BMI will not help lower your cost, but it will help improve your health.")


# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  analyze_smoker(smoker)
  analyze_bmi(bmi)
  return estimated_cost


# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name='Keanu', age=29, sex=1, bmi=26.2, num_of_children=3, smoker=1)


# printing every character with an even index
def print_some_characters(word):
  for i in range(len(word)):
    if i % 2 == 0:
      print(word[i])


print_some_characters("watermelon")

word = 'Gregor'
print(word.split('go'))


def count_multi_char_x(word, x):
  y = word.count(x)
  return y


print(count_multi_char_x("mississippi", "iss"))



txt = "Hello my friends"

x = txt.upper()

print(x)