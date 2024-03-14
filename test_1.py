from pooled_cohort import pooled_cohort_eq

class PatientClass:
    

risk = pooled_cohort_eq (  age = 55, 
                race = "w",
                gen = 'f',
                sbp = 120,
                hrx = False,
                tchol = 213,
                hdl = 50,
                dm = False,
                sm = False)

print (risk)