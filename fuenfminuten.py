import random
import sys
from markdown_pdf import MarkdownPdf, Section


def get_math_problem(operator = None):
    operators = ["+", "-"]
    if operator is None:
        operator = random.choice(operators)
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    # Ensure num1 is greater than num2 for subtraction
    if operator == "-":
        if num1 < num2:
            num1, num2 = num2, num1
        while (num1 >10) and (num1-num2 < 10):
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 20)
            if num1 < num2:
                num1, num2 = num2, num1


    if operator == "+":
        # Ensure the sum does not exceed 20
        while num1 + num2 > 20:
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 20)

    # Format the problem
    problem = {
        "num1": num1,
        "operator": operator,
        "num2": num2
    }

    return problem
def generate_math_problems(outfile: str):
        output = ""
        style = " table {table-layout: fixed; width: 100%;}\
        th, td {\
        border: 6px solid white;\
        font-size: 11px;\
        line-height: 1.6;\
        text-align: right;\
        width: 20%;\
            }"

        header = """
| Datum | _______________ |   |   |   |
| --- | --- | --- | --- | --- |\n"""
        output += header
        for i in range(10):  # 10 lines
            line = ""
            for _ in range(5):  # 5 problems per line
                if i % 2 == 0:
                    math_problem = get_math_problem("+")
                else:
                    math_problem = get_math_problem("-")
                line += f"{math_problem['num1']} {math_problem['operator']} {math_problem['num2']} = _____     | "
            output += "| " + line.strip() + " |\n"

        output += "\n\n-----------------------------------------\n\n"

        output += header
        for i in range(10):  # 10 lines
            line = ""
            for _ in range(5):  # 5 problems per line
                if i % 2 == 0:
                    math_problem = get_math_problem("+")
                else:
                    math_problem = get_math_problem("-")
                line += f"{math_problem['num1']} {math_problem['operator']} {math_problem['num2']} = _____     | "
            output += "| " + line.strip() + " |\n"

        pdf = MarkdownPdf()
        pdf.add_section(Section(output, paper_size="A4"), user_css = style)
        pdf.save(outfile)


if __name__ == "__main__":
    outfile = sys.argv[1] if len(sys.argv) > 1 else "output.pdf"
    generate_math_problems(outfile)

