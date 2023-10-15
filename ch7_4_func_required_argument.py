'''IN THIS CASE WE DONT PASS THE ARGUMENT WITH KEY VALUE SYNTAX AND ALSO IN ANY ORDER
    IN THIS THE FUNCTION CALL SHOULD STRICLY MATCH THE ARGUMENT IN THE FUNCTION DECLARATION '''

def personal_details(fname,lastname,location,id):
    print(f"name :{fname} {lastname}\nlocation :{location}\nid :{id}")

print("..........showing you the required argument example.........")
personal_details("rohit", "singh", "haridwar", 4)