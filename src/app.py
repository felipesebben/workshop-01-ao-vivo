from frontend import ExcelValidatorUI
from backend import process_excel
import logging

def main():
    ui = ExcelValidatorUI()
    ui.display_header()

    upload_file = ui.upload_file()

    if upload_file: # Só entra na condicional se o arquivo for carregado
        df, result, error = process_excel(upload_file)
        ui.display_results(result, error)

        if error:
            ui.display_wrong_message()
            logging.error("Planilha apresentava erro de schema.")
        elif ui.display_save_button():
            ui.display_success_message()
            logging.info("Planilha validada e salva no banco de dados.")

if __name__ == "__main__":
    main()