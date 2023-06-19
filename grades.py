import streamlit as st
import numpy as np

st.markdown('# Math 9 Grade Calculator')

st.markdown('## Essential Outcomes')

essout = st.multiselect("Select all EO's that you have completed:",["All Complete","EO1","EO2","EO3","EO4","EO5","EO6"])
if "All Complete" in essout:
    essout = ["EO1","EO2","EO3","EO4","EO5","EO6"]
essouttot = len(essout)


st.markdown('## General Outcomes')

geoutMa = st.multiselect("Select all MATLAB EO's that you have completed:",["All Complete","GOMa1","GOMa2","GOMa3","GOMa4","GOMa5"])
if "All Complete" in geoutMa:
    geoutMa = ["GOMa1","GOMa2","GOMa3","GOMa4","GOMa5"]
geoutMAtot = len(geoutMa)

geoutPy = st.multiselect("Select all MATLAB EO's that you have completed:",["All Complete","GOPy1","GOPy2","GOPy3","GOPy4","GOPy5"])
if "All Complete" in geoutPy:
    geoutPy = ["GOPy1","GOPy2","GOPy3","GOPy4","GOPy5"]
geoutPytot = len(geoutPy)

totalgo = geoutPytot + geoutMAtot

st.markdown('## Homework Assignments')

matlabhomework = st.multiselect("Select all MATLAB homeworks you have passed:",["All Complete","MLHW1","MLHW2","MLHW3","MLHW4"])
if "All Complete" in matlabhomework:
    matlabhomework = ["MLHW1","MLHW2","MLHW3","MLHW4"]

pyhomework = st.multiselect("Select all python homeworks you have passed:",["All Complete","PyHW 1","PyHW 2","PyHW 3","PyHW 4"])
if "All Complete" in pyhomework:
    pyhomework = ["PyHW 1","PyHW 2","PyHW 3","PyHW 4"]

pyhomeworktotal = len(pyhomework)
matlabhomeworktotal = len(matlabhomework)

totalhw = matlabhomeworktotal + pyhomeworktotal

st.markdown('## Lecture Quizzes')

videoquiztot = st.number_input("How many lecture quizzes do you have credit for?",min_value=0, max_value=104,step=1)

st.markdown('## Grade Computation')

#gradelist = [totalgo, matlabgos, pygos, totalhw, matlabhw, pyhw, videoquiz ]
studentgradelist = [totalgo,geoutMAtot,geoutPytot,totalhw, matlabhomeworktotal, pyhomeworktotal, videoquiztot]

def gradecheck(student):
    for grade in grades:
        for b in range(len(grades[grade])):
            print([student[a] in grades[grade][b][a] for a in range(7)])            
            total = sum([student[a] in grades[grade][b][a] for a in range(7)])
            if total == 7:
                return grade
    return None


Aplus = ([10],[5],[5],[8],[4],[4],[100])
A = (range(9,11),range(4,6),range(4,6),range(7,9),range(3,5),range(3,5),range(90,105))

#XOR 6 homeworks
Aminusv1 =(range(9,11),range(4,6),range(4,6),[6],range(3,5),range(3,5),range(90,105))

#XOR 8 outcomes
Aminusv2 = ([8],range(4,7),range(4,7),range(7,9),range(3,5),range(3,5),range(90,105))

#XOR 81-89 videos
Aminusv3 = (range(9,11),range(4,6),range(4,6),range(7,9),range(3,5),range(3,5),range(81,90))


Bplus = ([8],range(3,6),range(3,6),range(5,9),range(2,5),range(2,5),range(85,105))

B = (range(7,11),range(3,6),range(3,6),range(5,9),range(2,5),range(2,5),range(80,105))

#XOR 4 satisfactory homeworks
Bminusv1 = (range(7,11),range(3,6),range(3,6),range(4,9),range(2,5),range(2,5),range(80,105))

#XOR 6 GOs
Bminusv2 =(range(6,13),range(2,7),range(2,7),range(5,9),range(2,5),range(2,5),range(80,105))

#XOR 71-79 lecture quizzes
Bminusv3 = (range(7,11),range(3,6),range(3,6),range(5,9),range(2,5),range(2,5),range(71,80))


Cplus = (range(6,11),range(1,6),range(1,6),range(5,9),range(2,5),range(2,5),range(75,105))

C = (range(5,11),range(1,6),range(1,6),range(4,9),range(2,5),range(2,5),range(70,105))

#XOR 3 satisfactory homeworks
Cminusv1 = (range(5,11),range(1,6),range(1,6),range(3,9),range(1,5),range(1,5),range(70,105))

#XOR 4 GOs
Cminusv2 = (range(4,11),range(1,6),range(1,6),range(4,9),range(2,5),range(2,5),range(70,105))

#XOR <70 lecture quizzes
Cminusv3 = (range(5,11),range(1,6),range(1,6),range(4,9),range(2,5),range(2,5),range(0,70))

grades = {"A+":[Aplus,],"A":[A,],"A-":[Aminusv1,Aminusv2,Aminusv3],"B+":[Bplus,],"B":[B,],"B-":[Bminusv1,Bminusv2,Bminusv3],"C+":[Cplus,],"C":[C,],"C-":[Cminusv1,Cminusv2,Cminusv3]}

if essouttot != 6:
    st.write("All 6 EO's must be passed to pass the class. See syllabus for what happens in this case.")
else:
    if gradecheck(studentgradelist) is None:
        st.write("No grade returned. Perhaps you do not meet minimum requirements for any grade category. If you believe this is in error please contact your instructor.")
    else:
        grade = gradecheck(studentgradelist)
        st.write(f"Your grade: {grade}")
