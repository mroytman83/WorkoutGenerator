#Library Importation
import tkinter as tk
import csv
import math
import pandas as pd
import random
import copy
from PIL import Image, ImageTk
from itertools import count, cycle#parsing the csv database of exercises

def process_csv(filename):
    exampleFile = open(filename, encoding="utf-8")  
    exampleReader = csv.reader(exampleFile) 
    exampleData = list(exampleReader)        
    exampleFile.close()  
    return exampleData

#tidying the data
data=process_csv("fit_data.csv")
fit_data=pd.DataFrame(data[18:])

#bucketization starts here
back=fit_data[(fit_data[1]=="Back - Latissimus Dorsi") | (fit_data[1]=="Back - Lat.Dorsi/Rhomboids")]
back_exercises=list(back[2])

chest=fit_data[(fit_data[1].str.contains("Chest"))]
chest_exercises=list(chest[2])


bis=fit_data[(fit_data[1]=="Biceps")]
bicep_exercises=list(bis[2])

abdominal=fit_data[(fit_data[1].str.contains("Abdominals"))]
abdominal_exercises=list(abdominal[2])

quads=fit_data[(fit_data[1].str.contains("Quadriceps"))]
quad_exercises=list(quads[2])

hams=fit_data[(fit_data[1].str.contains("Hamstrings"))]
hams_exercises=list(hams[2])

triceps=fit_data[(fit_data[1]=="Triceps")]
tricep_exercises=list(triceps[2])

shoulders=fit_data[fit_data[1].str.contains("Shoulder")]
shoulder_exercises=list(shoulders[2])

posterior=fit_data[fit_data[1].str.contains("Erector Spinae")]
lower_back_exercises=list(posterior[2])

calves=fit_data[fit_data[1].str.contains("Calves")]
calve_exercises=list(calves[2])

#Dictionary #1 creation
exercise_dict={}
exercise_dict["Back"]=back_exercises
exercise_dict["Abs"]=abdominal_exercises
exercise_dict["Chest"]=chest_exercises
exercise_dict["Biceps"]=bicep_exercises
exercise_dict["Quadriceps"]=quad_exercises
exercise_dict["Hamstrings"]=hams_exercises
exercise_dict["Triceps"]=tricep_exercises
exercise_dict["Shoulders"]=shoulder_exercises
exercise_dict["Lower Back"]=lower_back_exercises
exercise_dict["Calves"]=calve_exercises
exercise_dict

#Dictionary #2 creation

routine_dict={}
routine_dict["Upper"]=["Chest", "Back", "Biceps", "Triceps", "Shoulders", "Abs"]
routine_dict["Lower"]=["Lower Back", "Calves","Hamstrings", "Quadriceps", "Abs"]
routine_dict["Legs"]=["Lower Back", "Calves","Hamstrings", "Quadriceps", "Abs"]
routine_dict["FullBody"]=["Chest", "Back", "Biceps", "Triceps", "Shoulders", "Abs", "Lower Back", "Calves","Hamstrings", "Quadriceps"]
routine_dict["ChestBack"]=["Chest", "Back",  "Abs"]
routine_dict["Push"]=["Chest", "Shoulders",  "Triceps", "Abs"]
routine_dict["Pull"]=["Back", "Lower Back", "Biceps", "Abs"]
routine_dict["ShoulderArms"]=["Shoulders", "Biceps", "Triceps", "Abs"]

#beginning of the interface
root=tk.Tk()
root.title('Workout Generator')
root["bg"]="yellow"
#creation of the gui
canvas= tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=5)
canvas["bg"]="blue"
#logo
logo=Image.open("zyzz.png")
logo=ImageTk.PhotoImage(logo)

#placing the logo inside a label widget
logo_label=tk.Label(image=logo)

logo_label.image=logo

#placing inside canvas
logo_label.grid( column=3, row=0)




#program instructions 
instructions=tk.Label(root, text="What Workout Are You Hitting Today: Upper, Lower, Pull, Push, Legs, FullBody, ChestBack, ShoulderArms?", font="Raleway")
instructions.grid(columnspan=3, column=2, row=1)

#entry button
entry1 = tk.Entry(root, width=20) 
entry1.grid(column=3, row=2)


def getWorkout():  
    my_msgone= entry1.get()
    workout_for_today={}
    for workout in routine_dict:
        if my_msgone.lower()==workout.lower():
            if workout=="ChestBack":
                for muscle_group in routine_dict[workout]:
                    if muscle_group=="Chest" or muscle_group=="Back":
                    #this is done in order to add more exercises per important muscle group
                    #aka compound movements of the workout
                        workout_for_today[muscle_group]=random.sample(exercise_dict[muscle_group], 2)
                    else:
                        workout_for_today[muscle_group]=random.choice(exercise_dict[muscle_group])
            elif workout=="FullBody":
                routine_dict[workout]=random.sample(routine_dict[workout], 5)
                for muscle_group in routine_dict[workout]:
                    workout_for_today[muscle_group]=random.choice(exercise_dict[muscle_group])
            elif workout=="Pull":
                for muscle_group in routine_dict[workout]:
                    if muscle_group=="Back":
                        workout_for_today[muscle_group]=random.sample(exercise_dict[muscle_group], 2)
                    else:
                        workout_for_today[muscle_group]=random.choice(exercise_dict[muscle_group])
                
            elif workout=="ShoulderArms":
                for muscle_group in routine_dict[workout]:
                    if muscle_group=="Shoulders":
                        workout_for_today[muscle_group]=random.sample(exercise_dict[muscle_group], 2)
                    else:
                        workout_for_today[muscle_group]=random.choice(exercise_dict[muscle_group])
                
            elif workout=="Upper":
                routine_dict[workout]=random.sample(routine_dict[workout], 5) 
                for muscle_group in routine_dict[workout]:
                    workout_for_today[muscle_group]=random.choice(exercise_dict[muscle_group])
            elif workout=="Push":
                for muscle_group in routine_dict[workout]:
                    if muscle_group=="Chest":
                        workout_for_today[muscle_group]=random.sample(exercise_dict[muscle_group], 2)
                    else:
                        workout_for_today[muscle_group]=random.choice(exercise_dict[muscle_group])
            else:
                for muscle_group in routine_dict[workout]:
                    workout_for_today[muscle_group]=random.choice(exercise_dict[muscle_group])

    global label1
    label1=tk.Label(root, text="Here is your Workout for Today:")
    label1.grid(column=3, row=5)
    global label2
    label2 = tk.Label(root, text=workout_for_today)
    label2.grid(column=3, row=6)
    global label3
    label3=tk.Label(root, text="Here are your rep ranges->"+ " Sets X Reps: "+str(random.randint(3,5))+"X"+str(random.randint(8,12)))
    label3.grid(column=3, row=7)
def emptify():
    label2.destroy()
    label3.destroy()
    label1.destroy()
        


#generate button
button2=tk.Button(text="Delete", command=emptify)
button1 = tk.Button(text='Generate', command=getWorkout)
button1.grid(column=2, row=3)
button2.grid(column=4, row=3)



#end command of the interface
root.mainloop()