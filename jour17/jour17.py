#=|=# Jour 17 de l'Advent of Code 2024 #=|=#
#=|=#      Commentaires sur l'exo      #=|=#
''' Pas drôle '''

# ========= INITIALIZATION ========== #
import re

A, B, C = 0, 1, 2

def lecture_fichier(fichier, fonction):
    try:
        with open(fichier, "r") as txt:
            return fonction(txt)
    except FileNotFoundError:
        print(f"Le fichier '{fichier}' est introuvable.")
        return None

def fichier_to_tab(fichier):
    program = []
    pattern = r"Register A: (\d+)\nRegister B: (\d+)\nRegister C: (\d+)\n\nProgram: ([\d,]+)"
    nums = re.findall(pattern, fichier.read())
    
    registers = [int(nums[0][0]),int(nums[0][1]),int(nums[0][2])]
    program = list(map(int, nums[0][3].split(',')))

    return registers,program

# ============= PART 1 ============= #
def resolve_operand(registers, operand):
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return registers[A]
        case 5:
            return registers[B]
        case 6:
            return registers[C]
        case _:
            raise ValueError(f"Operand {operand} unknown")

def apply_operator(registers, operand, operator, result):
    comboOperand = resolve_operand(registers, operand)

    match operator:
        case 0:  # adv
            # registers[A] //= (2 ** operand) # Meme operation en plus compliqué
            registers[A] = registers[A] >> comboOperand
        case 1:  # bxl
            registers[B] = registers[B] ^ operand
        case 2:  # bst
            registers[B] = comboOperand % 8
        case 3:  # jnz
            if registers[A] != 0:
                return comboOperand  # Sauter à une nouvelle position
        case 4:  # bxc
            registers[B] = registers[B] ^ registers[C]
        case 5:  # out
            result.append(comboOperand & 7)
        case 6:  # bdv
            registers[B] = registers[A] >> comboOperand
        case 7:  # cdv
            registers[C] = registers[A] >> comboOperand
        case _:
            raise ValueError(f"Operator {operator} unknown")
    return None

def evaluate(registers,program):
    output = []
    cursor = 0

    while cursor < len(program):
        operator = program[cursor]
        operand = program[cursor+1]

        jump = apply_operator(registers, operand, operator, output)
        if jump is not None:
            cursor = jump
        else:
            cursor += 2

    return output

def part_1(fichier):
    registers, program = fichier_to_tab(fichier)
    output = evaluate(registers,program)
    result = ",".join(map(str, output))
    print("Part 1 :",result)
    return result

# ============= PART 2 ============= #
# 1- Les chiffres du début sont plus faciles à changer
# 2- On remarque que si on fait x8 on ajoute une case à gauche de output valant 4
# 3- On économisera du temps de calcul si on construit la liste par la fin !!
def part_2(fichier):
    registers, program = fichier_to_tab(fichier)
    a = 1
    step = 1
    while True:
        registers[A] = a
        output = evaluate(registers, program)
        if output[-step:] == program[-step:]:
            #print(f"Trying A={a}, Output={output}, Objective={program}")
            if step == len(program):
                break
            step += 1
            a *= 8
        else:
            a += 1
    print("Part 2 :", a)

lecture_fichier("jour17/jour17.txt", part_2)
# Part 1 : 7,5,4,3,4,5,3,4,6 en 0.30 sec
# Part 2 : 164278899142333 en 0.34 sec