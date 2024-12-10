grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = ['Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron']
list(students)
#print(students)
A = grades[0]
B = grades[1]
J = grades[2]
K = grades[3]
S = grades[4]
#print(A,B,J,K,S)
sc_A = round((A[0]+A[1]+A[2]+A[3]+A[4])/len(A),2)
sc_B = round((B[0]+B[1]+B[2]+B[3])/len(B),2)
sc_J = round((J[0]+J[1]+J[2]+J[3])/len(J),2)
sc_K = round((K[0]+K[1]+K[2])/len(K),2)
sc_S = round((S[0]+S[1]+S[2]+S[3]+S[4])/len(S),2)
#print(sc_A,sc_B,sc_J,sc_K,sc_S)
Sch_mag = {}
Sch_mag[students[4]] = sc_A
Sch_mag[students[1]] = sc_B
Sch_mag[students[0]] = sc_J
Sch_mag[students[3]] = sc_K
Sch_mag[students[2]] = sc_S
print(Sch_mag)
