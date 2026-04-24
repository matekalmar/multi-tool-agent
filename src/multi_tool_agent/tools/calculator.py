import re
from langchain.tools import tool


def make_calculate_tool():
    @tool
    def calculate(expression: str) -> dict:
        """Matematikai számításokhoz"""

        try:
            expression = expression.strip()

            if not re.fullmatch(r"[0-9+\-*/(). ]+", expression):
                return {
                    "success": False,
                    "error": "Invalid characters in expression.",
                    "expression": expression
                }

            result = eval(expression, {"__builtins__": {}}, {})

            return {
                "success": True,
                "result": result,
                "expression": expression
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "expression": expression
            }
    return calculate