student_details={"name":"rohit",
                 "age":45,
                 "grade":9,
                 "subjects": ['math','english','history'],
                 "Address":{
                     "state":"jharkhand",
                     "street":"gopal nagar",
                     "city": "mosaboni",
                     "pincode":"832104"
                    }           
                            
                     
                }
print("assesing the dictonary elements")
print(f"student name={student_details['name']}")
print(f"student age={student_details['age']}")
print(f"grade ={student_details['grade']}")
print(f"Student Subjects: {', '.join(student_details['subjects'])}")
print(f"student address : {student_details['Address']['state']},{student_details['Address']['street']},{student_details['Address']['city']},{student_details['Address']['pincode']}")






