sbsu = "linguistics, physics, programming, fine arts"
stanford = "biology, classics, geophysics, music"
 
arts = "linguistics, fine arts, classics, music"
sciences = "physics, programming, biology, geophysics"
 
major = "biology"
if major in sbsu:
    if major in arts:
        print("This is an arts program at SBSU")
    if major in sciences:
        print("This is a sciences program at SBSU")
if major in stanford:
    if major in arts:
        print("This is an arts program at Stanford")
    if major in sciences:
        print("This is a sciences program at Stanford")
