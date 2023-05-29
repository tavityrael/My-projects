def aritmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''

    for problem in problems:
        parts = problem.split()
        if not (parts[0].isdigit() and parts[2].isdigit()):
            return 'Error: Numbers must only contain digits.'
        if not (parts[1] == '+' or parts[1] == '-'):
            return "Error: Operator must be '+' or '-'."
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        result = str(eval(problem))
        width = max(len(parts[0]), len(parts[2])) + 2
        line1 += parts[0].rjust(width) + '    '
        line2 += parts[1] + parts[2].rjust(width - 1) + '    '
        line3 += '-' * width + '    '
        line4 += result.rjust(width) + '    ' if show_answers else ''

    arranged_problems = line1.rstrip() +'\n' + line2.rstrip() + '\n' + line3.rstrip()
    if show_answers:
        arranged_problems += '\n' + line4.rstrip()

    return arranged_problems

problems = ['32 + 787', '212 - 22', '8488 + 33', '1000 - 99']
print(aritmetic_arranger(problems, True))