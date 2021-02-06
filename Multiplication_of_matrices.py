import numpy as np

print("\n\n\t\t\t***** MARTIX MULTIPLICATION CALCULATOR *****\t\t\n")
R = int(input("Enter number of rows of Matrix 'A':")) 
C = int(input("Enter number of columns of Matrix 'A':")) 
print(f"Enter {R*C} entries in a single line (separated by space): ") 
entries = list(map(int, input().split())) 
A = np.array(entries).reshape(R, C)
print("\nMatrix A is\n")
print(A) 

R1 = int(input("\nEnter the number of rows of Matrix 'B':")) 
C1 = int(input("Enter the number of columns of Matrix 'B':")) 
print(f"Enter {R1*C1} entries in a single line (separated by space): ") 
entries = list(map(int, input().split())) 
B = np.array(entries).reshape(R1, C1)
print("\nMatrix B is\n")
print(B) 

result = [[sum(a * b for a, b in zip(R, C1))  
                        for C1 in zip(*B)] 
                                for R in A] 
  
print("\nResultant Matrix ")
print("----------------")
for C in result:
   print(C)
