import logging

from backend import ExcelProcessor
from frontend import ExcelValidatorUI
import sentry_sdk

import sentry_sdk

sentry_sdk.init(
    dsn="https://1d01281930cd36dcaacb4d88d0d3ffe6@o4506864752590848.ingest.us.sentry.io/4506864774217728",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

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
            sentry_sdk.capture_message("Planilha apresentava erro de schema.")
        elif ui.display_save_button():
            bk.save_dataframe_to_sql(df)
            ui.display_success_message()
            logging.info("Planilha validada e salva no banco de dados.")
            sentry_sdk.capture_message("Planilha validada e salva no banco de dados.")


if __name__ == "__main__":
    main()
