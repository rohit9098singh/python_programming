class person:
    Name='harry'
    age=34
    occupation="undergraduate and learning codding"
    
    def info(self):
     print(f"{self.Name} is a {self.occupation}")
a=person()
print("Name=",a.Name,"\nage=",a.age,"\noccupation=",a.occupation)
a.info()

# self----> vo object jiske liye method call hora hai