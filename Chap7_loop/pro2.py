# WAP to greet all the person names stored in a list and which start with letter 's' 

name = ["Raj", "Sita", "Gita", "Hari", "Rina", "Suman"]
for greet in name:
    if greet.startswith('S') or greet.startswith('s'):
        print(f"Hello {greet}, Welcome to hood")