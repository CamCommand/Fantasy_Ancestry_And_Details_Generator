import tkinter as tk
from tkinter import messagebox
import random
import csv

with open('heritage.csv', 'r') as read_obj:
    # Create a CSV reader object
    csv_reader = csv.reader(read_obj)
    
    # Convert the CSV reader object to a list
    heritage_list_of_rows = list(csv_reader)
	
with open('age.csv', 'r') as read_obj:
    # Create a CSV reader object
    csv_reader = csv.reader(read_obj)
    
    # Convert the CSV reader object to a list
    age_list_of_rows = list(csv_reader)

with open('detail.csv', 'r') as read_obj:
    # Create a CSV reader object
    csv_reader = csv.reader(read_obj)
    
    # Convert the CSV reader object to a list
    detail_list_of_rows = list(csv_reader)
	
with open('gender.csv', 'r') as read_obj:
    # Create a CSV reader object
    csv_reader = csv.reader(read_obj)
    
    # Convert the CSV reader object to a list
    gender_list_of_rows = list(csv_reader)
	
with open('clothes.csv', 'r') as read_obj:
    # Create a CSV reader object
    csv_reader = csv.reader(read_obj)
    
    # Convert the CSV reader object to a list
    clothes_list_of_rows = list(csv_reader)

# Create the main application window
root = tk.Tk()  
root.title("Polzor NPC Maker")  # Set window title
root.geometry("700x800")  # Set window size

# Heritage Options
#heritage = ['A', 'B', 'C', 'D']
# Heritage Weights
# weights = [10, 30, 60, 150]

# puts heritages and weights into their own lists 
heritage_elements = [sublist[0] for sublist in  heritage_list_of_rows]
string_list = [sublist[1] for sublist in  heritage_list_of_rows]
# converts the weight into a int from a string
weight_elements = [int(x) for x in string_list]
#print(weight_elements)

# puts ages and weights into their own lists 
age_elements = [sublist[0] for sublist in  age_list_of_rows]
string_list2 = [sublist[1] for sublist in  age_list_of_rows]
# converts the weight into a int from a string
weight_elements2 = [int(x) for x in string_list2]

# puts physical details and weights into their own lists 
detail_elements = [sublist[0] for sublist in  detail_list_of_rows]
string_list3 = [sublist[1] for sublist in  detail_list_of_rows]
# converts the weight into a int from a string
weight_elements3 = [int(x) for x in string_list3]

# puts gender and weights into their own lists 
gender_elements = [sublist[0] for sublist in  gender_list_of_rows]
string_list4 = [sublist[1] for sublist in  gender_list_of_rows]
# converts the weight into a int from a string
weight_elements4 = [int(x) for x in string_list4]

# puts clothes on the NPC and weights into their own lists 
clothes_elements = [sublist[0] for sublist in  clothes_list_of_rows]
string_list5 = [sublist[1] for sublist in  clothes_list_of_rows]
# converts the weight into a int from a string
weight_elements5 = [int(x) for x in string_list5]

# List to store npc
npc = []

def get_NPC():
    #result = random.choices(heritage, weights=weights, k=1)
	#npc.append(heritage_result)
	
	heritage_result = random.choices(heritage_elements, weights=weight_elements, k=1)# adds heritage
	age_result = random.choices(age_elements, weights=weight_elements2, k=1)		# Adds age
	detail_result = random.choices(detail_elements, weights=weight_elements3, k=1)	# Adds detail
	gender_result = random.choices(gender_elements, weights=weight_elements4, k=1)	# Adds gender
	clothes_result = random.choices(clothes_elements, weights=weight_elements5, k=1)# Adds clothes
	
	NPC_final = "A ", age_result, ' ', detail_result, ' ', heritage_result, " who is a ", gender_result, ' that is ', clothes_result
	#NPC_final = ' '.join(NPC_final)
	npc_listbox.insert(tk.END, heritage_result, age_result, detail_result, gender_result, clothes_result, '________________________ \n')  # Display task in the listbox
	print(NPC_final)

def clear():
	npc_listbox.delete(0,'end')

add_button = tk.Button(root, text="Generate NPC", command=get_NPC)  # Button to add npc
add_button.pack(pady=10)

add_button2 = tk.Button(root, text="Clear", command=clear)  # Button to add npc
add_button2.pack(pady=10)

npc_listbox = tk.Listbox(root, width=60, height=315)  # Listbox to display npc
npc_listbox.pack(pady=10)  # Add spacing around the listbox

# Run the application
root.mainloop()