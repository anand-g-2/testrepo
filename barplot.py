import matplotlib.pyplot as plt		
import numpy as np 
objects='Python', 'C', 'C++', 'Java'
#x_pos = np.arange(len(objects)) 	
no_of_students = [10,8,6,4] 
plt.bar(objects, no_of_students, align='center',alpha=0.8)
#plt.xticks(x_pos, objects1) 	
plt.ylabel('Number of students') 
plt.title('Programming language usage') 
plt.show()
