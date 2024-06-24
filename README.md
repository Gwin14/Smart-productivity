# Smart Productivity

Smart Productivity é uma aplicação web desenvolvida para melhorar a produtividade, fornecendo funcionalidades de criação e gerenciamento de notas.

## Funcionalidades

- **Criação e edição de notas:** Adicione, edite e exclua suas notas.
- **Suporte a tags:** Organize suas notas com tags.
- **Interface amigável:** Interface de usuário limpa e intuitiva.

## Estrutura do Projeto

```bash
Smart-productivity-main/
├── base_static/
│   └── global/
│       └── css/
│           └── style.css
├── base_templates/
│   └── global/
│       └── base.html
│       └── partials/
│           └── _header.html
├── notesApp/
│   ├── migrations/
│   ├── templates/
│   │   └── notesApp/
│   │       └── index.html
│   │       └── note_detail.html
│   │       └── partials/
│   │           └── _sideNotes.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .gitignore
├── LICENSE
├── manage.py
└── README.md
```

## Requisitos

- Python 3.x
- Django 3.x

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/Smart-productivity.git
```

2. Navegue até o diretório do projeto:

```bash
cd Smart-productivity-main
```

3. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate # No Windows, use `venv\Scripts\activate`
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Realize as migrações do banco de dados:

```bash
python manage.py migrate
```

6. Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

7. Acesse a aplicação em seu navegador:

```
http://127.0.0.1:8000/
```

## Uso

1. Crie uma conta ou faça login.
2. Adicione, edite e organize suas notas usando a interface da aplicação.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Agradecimentos

A todos que contribuíram para este projeto.

---

Você pode personalizar este README.md conforme necessário, incluindo informações adicionais específicas do seu projeto.
