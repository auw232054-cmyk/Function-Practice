#Write a function that receives a dictionary of scores and returns a new dictionary containing only passing students.
def score_dictionary(name,passing_score=60):
    passing_students={}
    for name,score in name.items():
        if score>=passing_score:
            passing_students[name]=score
    return passing_students
print(score_dictionary({"mina": 100, "bob": 50}))


