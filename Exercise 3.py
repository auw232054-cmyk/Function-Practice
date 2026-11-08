#Write a function that accepts a name, major and optional country and returns a student dictionary. Use "Bangladesh" as the default country.
def student_information(name,major,country='Bangladesh'):
    return {'name':name,'major':major,'country':country}

print(student_information('mina','cs','afghanistan'))