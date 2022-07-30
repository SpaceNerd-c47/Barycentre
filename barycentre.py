# Programe for determining the Barycentre between two bodies.
print("Programe for determining the barycentre between two bodies")
# a is the distance between the centre of your two chosen bodies
# is input for "a" in 10^6km or AU?
unit_question = input("is input for 'a' in 10^6km or AU? km/AU")
if unit_question == "AU":
    a_unit = 149597871
else:
    a_unit = 10**6
# is input for "m1" & "m2" in 10^24kg or Msun?
unit_question2 = input("is input for 'm1' & 'm2' in 10^24kg or Msun? kg/Msun")
if unit_question2 == "Msun":
    m_unit = 1988500*(10**24)
else:
    m_unit = 10**24
# do you know the mean difference between Apogee and Perigee?
question_input = input("do you know the mean difference between Apogee and Perigee? y/n ")
if question_input == "n":
    # enter Apogee value
    apogee_input = float(input("input apogee value: "))
    # enter Perigee value
    perigee_intup = float(input("input perigee value: "))
    # a = (Apogee+Perigee)/2
    a_value = (apogee_input + perigee_intup)/2
else:
    a_value = float(input("input a: "))
a = a_value*a_unit
# m2 is the lower mass of your chosen bobies (10^24 kg)
m2_input = float(input("input m2: "))
# now we convert from 10^24 kg to kg
m2 = m2_input*m_unit
# m1 is the higher mass of your chosen bodies  (10^24 kg)
m1_input = float(input("input m1: "))
# now we convert from 10^24 kg to kg
m1 = m1_input*m_unit
# r1 is the distance from the centre of m1 to barycentre
r1 = a/(1+(m1/m2))
print(f"distance between the centre of m1 and the barycentre: {r1/149597871} AU or {r1} km")