import pandas as pd
from langchain.tools import tool
from ..context import AppContext

def make_analyze_csv_tool(context: AppContext):
    numeric_operations = {"mean", "sum", "min", "max"}

    @tool
    def analyze_csv(operation: str, column: str = None, rows: int = 5) -> dict:
        """A betöltött CSV elemzéséhez"""
        try:
            df = context.df
            allowed_operations = context.config.allowed_operations

            if operation not in allowed_operations:
                raise ValueError(
                    f"Ismeretlen művelet. Elérhető műveletek: {allowed_operations}"
                )

            if operation in numeric_operations:
                if column is None:
                    raise ValueError("A numerikus művelethez kell oszlopnév.")

                if column not in df.columns:
                    raise ValueError(
                        f"Az oszlop nem található. Elérhető oszlopok: {df.columns.tolist()}"
                    )

                if not pd.api.types.is_numeric_dtype(df[column]):
                    raise ValueError("Az oszlop nem numerikus.")

                result = getattr(df[column], operation)()

            elif operation == "row_count":
                result = len(df)

            elif operation == "column_list":
                result = df.columns.tolist()

            elif operation == "head":
                result = df.head(rows).to_dict(orient="records")

            if hasattr(result, "item"):
                result = result.item()

            return {
                "success": True,
                "operation": operation,
                "result": result,
            }

        except Exception as e:
            return {
                "success": False,
                "operation": operation,
                "error": str(e),
            }

    return analyze_csv