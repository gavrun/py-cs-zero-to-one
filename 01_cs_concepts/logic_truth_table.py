# 01_cs_concepts/logic_truth_table.py

# Truth tables generated

def truth_table():
    """
    Draws neat ASCII table with frames and cells like in classic CLI interfaces
    """
    headers = ["A", "B", "A AND B", "A OR B", "NOT A"]
    rows = []
    for A in [True, False]:
        for B in [True, False]:
            row = [str(A), str(B), str(A and B), str(A or B), str(not A)]
            rows.append(row)

    # Calculate column widths
    col_widths = [max(len(str(cell)) for cell in col) for col in zip(headers, *rows)]

    # Build line helpers
    def build_separator():
        return "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"

    def build_row(row):
        return "|" + "|".join(f" {val.ljust(w)} " for val, w in zip(row, col_widths)) + "|"

    # Print table
    print(build_separator())
    print(build_row(headers))
    print(build_separator())
    for row in rows:
        print(build_row(row))
    print(build_separator())

# Generate
truth_table()

