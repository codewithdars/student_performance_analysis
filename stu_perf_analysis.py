import matplotlib.pyplot as plt
import pandas as pd

data = {
    "student": ["A","B","C","D","E","F","G","H","I","J","K","L"],
    "age": [18,19,18,20,19,21,20,18,19,20,21,19],
    "marks": [72,85,64,91,78,88,69,95,82,76,90,68],
    "attendance": [82,91,75,96,88,93,79,97,89,84,95,73],
    "department": [
        "CSE","AI","CSE","ECE","AI","CSE",
        "ECE","AI","CSE","ECE","AI","CSE"
    ]
}

df = pd.DataFrame(data)

total_students = df['student'].count()
print("total_students = ", total_students)    
print("average_marks = ", df['marks'].mean())
print("highest_marks = ", df['marks'].max())
print("lowest_marks = ", df['marks'].min())
print("average_attendance = ", df['attendance'].mean())
print("no. of students in each department = ", df['department'].value_counts())

# Student Marks Analysis

plt.plot(df['student'], df['marks'], marker='o', linestyle='-', color='b')
plt.title('Student Marks Analysis')
plt.xlabel('Student')       
plt.ylabel('Marks')
# plt.show()

#Average marks by department


dept_avg = df.groupby('department')['marks'].mean()
dept_avg.plot(kind='bar', color='orange')
plt.title('Average Marks by Department')
plt.xlabel('Department')    
plt.ylabel('Average Marks')
plt.show()


# #Histrogram :

plt.hist(df['marks'], bins=10, color='green', edgecolor='black')
plt.title('Marks Distribution') 
plt.xlabel('Marks')
plt.ylabel('Number of Students')    
plt.show()

# #scatter plot of marks vs attendance

plt.scatter(df['marks'], df['attendance'], color='purple')
plt.title('Marks vs Attendance')
plt.xlabel('Marks')
plt.ylabel('Attendance')
plt.show()

# # 2*2 Dashboard : subplots

fig,axs = plt.subplots(2,2, figsize=(10,8))
axs[0,0].plot(df['student'], df['marks'], marker='o', linestyle='-', color='b')
axs[0,0].set_title('Student Marks Analysis')   
axs[0,1].plot(df['attendance'],marker='o', linestyle='-', color='g')
axs[0,1].set_title('Attendance Analysis')
axs[1,0].plot(df['age'],marker='o', linestyle='-', color='r')
axs[1,0].set_title('Age Analysis')
axs[1,1].bar(df.groupby('department')['marks'].mean().index, df.groupby('department')['marks'].mean().values, color='orange')
axs[1,1].set_title('dept avg marks bar plot ')
plt.suptitle('Student Performance Analysis Dashboard')
plt.show()

# # challenge: add a new column "performance" :


performance = []
for mark in df['marks']:
    if mark < 60:
        performance.append('Poor')
    elif mark < 70:
        performance.append('Average')
    elif mark < 80:
        performance.append('Good')
    elif mark < 90:
        performance.append('Very Good')
    else:
        performance.append('Excellent')
df['performance'] = performance

print(df[['student', 'marks', 'performance']])

print("no. of students in each performance category = ", df['performance'].value_counts())
plt.pie(df['performance'].value_counts(), labels=df['performance'].value_counts().index, autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
plt.title('Performance Category Distribution')
plt.show()

#final challenge : create one final figure containning 4 subplots :

fig, axs = plt.subplots(2, 2, figsize=(12, 10))
dept_avg.plot(kind='bar', ax=axs[0, 0], color='orange')
axs[0, 0].set_title('Average Marks by Department')
attendance_avg = df.groupby('department')['attendance'].mean()
attendance_avg.plot(kind='bar', ax=axs[0, 1], color='green')
axs[0, 1].set_title('Average Attendance by Department')
df['performance'].value_counts().plot(kind='pie', ax=axs[1, 0], autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
axs[1, 0].set_title('Performance Category Distribution')
axs[1, 1].scatter(df['marks'], df['attendance'], color='purple')
axs[1, 1].set_title('Marks vs Attendance')  
plt.suptitle('Student Performance Analysis Dashboard')
plt.tight_layout()  
plt.show()