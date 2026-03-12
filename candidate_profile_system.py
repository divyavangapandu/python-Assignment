class PersonalInfo:
    def __init__(self,name,dob,phone,email):
        self.name=name
        self.dob=dob
        self.phone=phone
        self.email=email

class Education(PersonalInfo):
    def __init__(self,name,dob,phone,email,degree,univ,year,cgpa):
        super().__init__(name,dob,phone,email)
        self.degree=degree
        self.univ=univ
        self.year=year
        self.cgpa=cgpa

class Experience(Education):
    def __init__(self,name,dob,phone,email,degree,univ,year,cgpa,company,role,exp,skills):
        super().__init__(name,dob,phone,email,degree,univ,year,cgpa)
        self.company=company
        self.role=role
        self.exp=exp
        self.skills=skills

    def display(self):
        print("\n----- Candidate Profile -----")
        print("Name:",self.name)
        print("Date of Birth:",self.dob)
        print("Contact Number:",self.phone)
        print("Email:",self.email)

        print("\n--- Education Details ---")
        print("Degree:",self.degree)
        print("University:",self.univ)
        print("Year of Graduation:",self.year)
        print("CGPA:",self.cgpa)

        print("\n--- Work Experience ---")
        print("Company Name:",self.company)
        print("Job Role:",self.role)
        print("Years of Experience:",self.exp)
        print("Skills:",self.skills)

        if self.exp>5:
            print("Eligible for Senior Role")
        else:
            print("Eligible for Junior Role")


c1=Experience("Divya","14-06-2004","9885089135","divya@email.com",
              "B.Tech","ANITS",2018,9.5,
              "Infosys","Software Engineer",6,"Python, Java")

c2=Experience("Anitha","04-12-2005","9123456780","anitha@email.com",
              "BSc Computer Science","Andhra University",2021,9.2,
              "TCS","Junior Developer",2,"Python, SQL")

c1.display()
c2.display()
