#=|=# Jour 3 de l'Advent of Code 2024 #=|=#

def lecture_fichier(fichier,fonction):
    try:
        with open(fichier, "r",encoding="utf-8") as txt:
            fonction(txt)
    except FileNotFoundError:
        print(f"Le fichier '{fichier}' est introuvable.")

# ============= PART 1 ============= #
import re
import io

def find_pattern_1(fichier):
    pattern = r"mul\((\d+),(\d+)\)"
    if isinstance(fichier,io.TextIOWrapper):
        matches = re.findall(pattern, fichier.read())
    elif isinstance(fichier,str):
        matches = re.findall(pattern, fichier)
    else:
        matches = []
        print("Format attendu de fichier dans find_pattern_1 est str ou io.TextIOWrapper")
        print("Le format donne est",type(fichier))
        return 0
    nums = [(int(num[0]), int(num[1])) for num in matches]

    result = 0
    for i in range(len(nums)):
        result = result + (nums[i][0]*nums[i][1])

    print(result)
    return result

# ============= PART 2 ============= #
def find_pattern_2(fichier):
    texteModifie = fichier.read()
    texteModifie = texteModifie.replace("\n", "")
    texteModifie = re.sub(r"don't\(\).*?do\(\)","REMPLACED", texteModifie)
    texteModifie = re.sub(r"don't\(\).*","REMPLACED_END", texteModifie)

    #write_txt_from_str(texteModifie,"test")
    return find_pattern_1(texteModifie)

def write_txt_from_str(content, name):
    with open(f"jour3/{name}.txt", "w", encoding="utf-8") as txt:
        txt.write(content)

lecture_fichier("jour3/jour3.txt",find_pattern_2)