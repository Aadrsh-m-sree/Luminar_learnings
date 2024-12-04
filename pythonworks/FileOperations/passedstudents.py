f1=open("C:\\Users\\ajay\\Desktop\\pythonworks\\datasets\\all_students.txt")
f2=open("C:\\Users\\ajay\\Desktop\\pythonworks\\datasets\\failed.txt")
all_students=set([(st.rstrip("\n")) for st in f1])
failed_students=set([(st.rstrip("\n")) for st in f2])
all_passed=all_students.difference(failed_students)
f1.close()
f2.close()
print(all_passed)
