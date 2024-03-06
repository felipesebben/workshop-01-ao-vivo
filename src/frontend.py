import streamlit as st


class ExcelValidatorUI:

    def __init__(self):
        self.set_page_config()

    def set_page_config(self):
        """
        Define as configurações da página do Streamlit.
        """
        st.set_page_config(page_title="Validador de schema excel")

    def display_header(self):
        """
        Exibe o cabeçalho da aplicação.
        """
        st.title("Validador de schema excel")

    def upload_file(self):
        """
        Executa a função de upload do arquivo Excel.
        """
        return st.file_uploader("Carregue seu arquivo Excel aqui", type=["xlsx"])

    def display_results(self, result, error):
        """
        Retorna o resultado da validação do schema do arquivo Excel. Em caso de erro, exibe a mensagem de erro.

        - result: `bool`
        - error: `str`

        """
        if error:
            st.error(f"Erro na validação: {error}")
        else:
            st.success("O schema do arquivo Excel está correto!")

    def display_save_button(self):
        """
        Exibe o botão para salvar os dados no banco de dados.
        """
        return st.button("Salvar no Banco de Dados")

    def display_wrong_message(self):
        """
        Exibe a mensagem de erro caso a planilha não esteja correta.
        """
        return st.error("Necessário corrigir a planilha!")

    def display_success_message(self):
        """
        Exibe a mensagem de sucesso caso a planilha esteja correta.
        """
        return st.success("Dados salvos com sucesso no banco de dados!")
