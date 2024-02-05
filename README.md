# workshop-01-ao-vivo

## Instalação e Configuração
1. Clone o repositório:
```bash
git clone https://github.com/felipesebben/workshop-01-ao-vivo.git
cd workshop-01-ao-vivo

```
2. Configure a versão correta do Python com pyenv:
```bash
pyenv install 3.11.3
pyenv local 3.11.3
```
3. Instale as dependências do projeto:
```bash
poetry install
```
4. Ative o ambiente virtual:
```bash
poetry shell
```
5. Execute os testes para garantir que tudo está funcionando como esperado:
```bash
task test
```
6. Execute o comando para ver a documentação do projeto:
```bash
task doc
```
7. Execute o comando de execucão da pipeline para realizar a ETL:
```bash
task run
```
8. Verifique na pasta data/output se o arquivo foi gerado corretamente.

## Contato
Para dúvidas, sugestões ou feedbacks:

Felipe Sebben - felipesebben@yahoo.com.br / sebbencomdoisb@gmail.com
