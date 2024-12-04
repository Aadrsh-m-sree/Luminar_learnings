f_years=open("C:\\Users\\ajay\\Desktop\\pythonworks\\datasets\\years.txt","r")
f_leap=open("C:\\Users\\ajay\\Desktop\\pythonworks\\datasets\\leap_years.txt","w")
f_century=open("C:\\Users\\ajay\\Desktop\\pythonworks\\datasets\\century_years.txt","w")

def is_century_year(year):
    return True if year%100==0 else False

def is_leap_year(year):
    return True if year%100==0 and year%400==0 or year%100!=0 and year%4==0 else False

for year in f_years:
    year=int(year)
    if is_century_year(year):
        f_century.write(str(year)+"\n")
    if is_leap_year(year):
        f_leap.write(str(year)+"\n")
        
f_years.close()
f_century.close()
f_leap.close()
