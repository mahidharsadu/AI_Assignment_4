districts = [
    "Adilabad","Bhadradri_Kothagudem","Hyderabad","Jagtial","Jangaon",
    "Jayashankar_Bhupalpally","Jogulamba_Gadwal","Kamareddy","Karimnagar",
    "Khammam","Kumuram_Bheem","Mahabubabad","Mahabubnagar","Mancherial",
    "Medak","Medchal","Mulugu","Nagarkurnool","Nalgonda","Narayanpet",
    "Nirmal","Nizamabad","Peddapalli","Rajanna_Sircilla","Rangareddy",
    "Sangareddy","Siddipet","Suryapet","Vikarabad","Wanaparthy",
    "Warangal_Rural","Warangal_Urban","Yadadri_Bhongir"
]

neighbors = {
    "Adilabad": ["Kumuram_Bheem","Nirmal","Mancherial"],
    "Kumuram_Bheem": ["Adilabad","Mancherial"],
    "Mancherial": ["Adilabad","Kumuram_Bheem","Peddapalli","Nirmal"],
    "Nirmal": ["Adilabad","Mancherial","Jagtial"],
    "Jagtial": ["Nirmal","Karimnagar","Rajanna_Sircilla","Nizamabad"],
    "Rajanna_Sircilla": ["Karimnagar","Jagtial"],
    "Karimnagar": ["Peddapalli","Jagtial","Rajanna_Sircilla","Warangal_Urban"],
    "Peddapalli": ["Mancherial","Karimnagar","Warangal_Urban"],
    "Nizamabad": ["Jagtial","Kamareddy"],
    "Kamareddy": ["Nizamabad","Medak","Siddipet"],
    "Medak": ["Kamareddy","Sangareddy","Siddipet"],
    "Sangareddy": ["Medak","Rangareddy","Vikarabad","Medchal"],
    "Medchal": ["Hyderabad","Rangareddy","Sangareddy"],
    "Hyderabad": ["Medchal","Rangareddy"],
    "Rangareddy": ["Hyderabad","Medchal","Sangareddy","Vikarabad","Mahabubnagar"],
    "Vikarabad": ["Sangareddy","Rangareddy","Mahabubnagar"],
    "Mahabubnagar": ["Rangareddy","Vikarabad","Narayanpet","Wanaparthy","Jogulamba_Gadwal"],
    "Narayanpet": ["Mahabubnagar"],
    "Jogulamba_Gadwal": ["Mahabubnagar","Wanaparthy"],
    "Wanaparthy": ["Mahabubnagar","Nagarkurnool","Jogulamba_Gadwal"],
    "Nagarkurnool": ["Wanaparthy","Nalgonda"],
    "Nalgonda": ["Nagarkurnool","Suryapet","Yadadri_Bhongir"],
    "Yadadri_Bhongir": ["Nalgonda","Siddipet"],
    "Siddipet": ["Medak","Kamareddy","Yadadri_Bhongir","Jangaon"],
    "Jangaon": ["Siddipet","Warangal_Rural"],
    "Warangal_Rural": ["Jangaon","Warangal_Urban","Mahabubabad"],
    "Warangal_Urban": ["Warangal_Rural","Karimnagar","Peddapalli","Mulugu"],
    "Mulugu": ["Warangal_Urban","Jayashankar_Bhupalpally"],
    "Jayashankar_Bhupalpally": ["Mulugu"],
    "Mahabubabad": ["Warangal_Rural","Khammam"],
    "Khammam": ["Mahabubabad","Bhadradri_Kothagudem","Suryapet"],
    "Bhadradri_Kothagudem": ["Khammam"],
    "Suryapet": ["Nalgonda","Khammam"]
}

colors = ["Red","Green","Blue","Yellow"]

assignment = {}

def get_unassigned():
    for d in districts:
        if d not in assignment:
            return d
    return None

def is_safe(district,color):
    if district not in neighbors:
        return True
    for n in neighbors[district]:
        if n in assignment and assignment[n] == color:
            return False
    return True

def solve():
    if len(assignment) == len(districts):
        return True
    district = get_unassigned()
    for color in colors:
        if is_safe(district,color):
            assignment[district] = color
            if solve():
                return True
            del assignment[district]
    return False

result = solve()

if result:
    print("Telangana Map Coloring Solution:\n")
    for d in districts:
        print(d,"->",assignment[d])
else:
    print("No solution found")
