from frontend import ExcelValidatorUI
from backend import process_excel

def main():
    ui = ExcelValidatorUI()
    ui.display_header()

    upload_file = ui.upload_file()

    if upload_file: #só entra na condicional se o arquivo for carregado
        result, errors = process_excel(upload_file)
        ui.display_header(result, errors)

if __name__ == "__main__":
    main()