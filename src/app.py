import logging

from backend import ExcelProcessor
from frontend import ExcelValidatorUI


def main():
    ui = ExcelValidatorUI()
    bk = ExcelProcessor()
    ui.display_header()

    upload_file = ui.upload_file()

    if upload_file:  # Só entra na condicional se o arquivo for carregado
        df, result, errors = bk.process_excel(upload_file)
        ui.display_results(result, errors)

        if errors:
            ui.display_results(result, error=errors)
            logging.error("Planilha apresentava erro de schema.")
        elif ui.display_save_button():
            bk.save_dataframe_to_sql(df)
            ui.display_success_message()
            logging.info("Planilha validada e salva no banco de dados.")


if __name__ == "__main__":
    main()
