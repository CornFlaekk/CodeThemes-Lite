import random, os

def main():
    # Abre el fichero de origen
    with open("shuffle_comments.csv", "r") as f_origen:
        # Lee todas las líneas del fichero
        lines = f_origen.readlines()

    for folder in os.listdir("."):
        if os.path.isdir(folder):
            with open(os.path.join(".",folder, "comments.csv"), "w") as f_output:
                f_output.write("rating; comment\n")
                for i in range(random.randint(5,50)):
                    line = random.choice(lines)
                    f_output.write(line)
                

if __name__ == "__main__":
    main()

