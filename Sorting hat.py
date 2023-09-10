import time

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print('===============')
print('The Sorting Hat')
print('===============')

#Q1

print("Q1. Do you like Dawn or Dusk?")
print("1. Dawn")
print("2. Dusk")

answer = int(input('Enter answer (1-2): '))

if answer == 1:
  gryffindor += 1
  ravenclaw += 1
elif answer == 2:
  hufflepuff += 1
  slytherin += 1
else:
  print("Wrong input")

#Q2

print("\nQ2. When I'm dead, I want people to remember me as: ")
print("1. The good")
print("2. The great")
print("3. The wise")
print("4. The bold")

answer = int(input("Enter Answer (1-4): "))

if answer == 1:
  hufflepuff += 2

elif answer == 2:
  slytherin += 2

elif answer == 3:
  ravenclaw += 2

elif answer == 4:
  gryffindor += 2

else: 
  print("Wrong input")

#Q3

print("\nQ3. Which kind of instrument most pleases your ear? ")
print("1. The violin")
print("2. The trumpet")
print("3. The piano")
print("4. The drum")

answer = int(input('Enter your answer (1-4): '))

if answer == 1:
  slytherin += 4

elif answer == 2:
  hufflepuff += 4

elif answer == 3:
  ravenclaw += 4

elif answer ==4:
  gryffindor += 4

else:
  print("Wrong input")

  #Q4

print("\nQ4. Forest or river? ")
print("1. Forest")
print("2. River")

answer = int(input('Enter your answer (1-2): '))

if answer == 1:
  gryffindor += 1
  ravenclaw += 1

elif answer == 2:
  hufflepuff += 1
  slytherin += 1

else: 
  print("Wrong input")

#Q5

print("\nQ5. Moon or stars? ")
print("1. Moon")
print("2. Stars")

answer = int(input('Enter your answer (1-2): '))

if answer == 1:
  ravenclaw += 2
  slytherin += 2

elif answer == 2:
  gryffindor += 2
  hufflepuff += 2

else:
  print("Wrong input")

# results

most_points = max(gryffindor, ravenclaw, hufflepuff, slytherin) # We'll learn about max() in the Functions chapter

if gryffindor == most_points:
  print('Gryffindor!')
elif ravenclaw == most_points:
  print('Ravenclaw!')
elif hufflepuff == most_points:
  print('Hufflepuff!')
else:
  print('Slytherin!')

  time.sleep(60)