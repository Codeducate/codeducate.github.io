# Description
print ('Medical Allergy record management system');
print('System stores the records of patients and medicine ingredients they are allergic to.')
print ('Before prescribing a new medicine, doctors will use this system to check if  the patient is allergic to ingredients in that medicine')
print ('Modes of operation: Mode 1 : Patient and medcine evaluation, Mode 2 : add new patient data , Mode 3 : exit program')

# Preloaded data about patient and allergy
medicalrecords = {'jamie':'sulfa', \
'ben':'penicillin', 'sarah':'sulfa', \
'kim':'ibuprofen', 'blake':'asprin', 'ava':'amoxicillin', 'chloe':'asprin'}

while True:
  # take input related to patient name and medicine ingredient
  # Modes of operation: Mode 1 : Patient and medcine evaluation, Mode 2 : add new patient data , Mode 3 : exit program
  mode=input('Enter mode : ')

  # Decision making to determine if medcine can be prescribed
  if (mode==1):
    patient = raw_input('Enter patient name : ')
    ingredient=raw_input('Enter ingredient : ')
    print ('Patient name ' + patient)
    print ('Ingredient name ' + ingredient)
    # Check if patient data exists
    if patient.lower() in medicalrecords:
      # If data exists then check if patient is allergic
      if (ingredient.lower() == (medicalrecords[patient.lower()]).lower()):
         print('Do not prescribe ' + ingredient + ' to  ' +   patient + ' since patient is allergic')
      else :
         print('You can prescribe ' + ingredient + ' to  ' +   patient + ' since patient is not allergic')
    else:
     print('Data for patient ' +   patient + ' is not in system')
  # Add new patient data
  elif (mode==2):
    patient = raw_input('Enter patient name : ')
    ingredient=raw_input('Enter ingredient : ')
    print ('Patient name ' + patient)
    print ('Ingredient name ' + ingredient)
    # Add new patient data
    medicalrecords[patient.lower()] = ingredient.lower()
    print (medicalrecords)
  # Exit the program
  elif (mode==3):
     print ('Mode 3, Exiting program')
     break;
  else :
     print ('Incorrect mode, try again')