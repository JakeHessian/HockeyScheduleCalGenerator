import tabula

def extract_tables_from_pdf(pdf_filename):
    # Extract tables from PDF into a list of dataframes
    tables = tabula.read_pdf(pdf_filename, pages='all', multiple_tables=True)
    return tables

# Example usage
pdf_filename = "schedule.pdf"
extracted_tables = extract_tables_from_pdf(pdf_filename)

for i, table in enumerate(extracted_tables):
    print(f"Table {i + 1}:")
    print(table)
    print("\n" + "-"*50 + "\n")

    
