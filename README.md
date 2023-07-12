# Rotten Reviews!

Cadastro de filmes e reviews (como o RottenTomatoes) integrando FastAPI e um banco de dados mySQL. Inicialmente uma atividade de Megadados (6° Semestre de Engenharia de Computação do Insper), foi refeito posteriormente adicionando algumas features.

## Setup

1. Clone o repositório
   
    ```bash
    git clone https://github.com/gabrielonishi/rotten-reviews.git
    cd rotten-reviews/
    ```

2. Esse projeto utiliza de um ambiente virtual para garantir a estabilidade de versões. Crie um ambiente virtual python
   
    - MacOS/Linux
        ```bash
        python3 -m venv env
        source env/bin/activate
        ```
    - Windows
        ```bash
        python3 -m venv env
        .\env\Scripts\activate
        ```
3. Instale as dependências
   
    ```bash
        pip install -r requirements.txt
    ``` 

## Rodando o servidor

Você pode rodar o servidor uvicorn localmente usando

```bash
uvicorn main:app --reload
```