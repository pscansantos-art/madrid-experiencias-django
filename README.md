# Madrid Experiências - Guia Turístico Web

Aplicação web desenvolvida com a arquitetura **Django (MVT)** focada no turismo da cidade de Madrid, destacando seus principais pontos históricos, culturais e a tradição futebolística no Estádio Santiago Bernabéu.

🔗 **Link do Projeto Ao Vivo:** [pscansantos.pythonanywhere.com](https://pscansantos.pythonanywhere.com)

---

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python 3.10 / Django
- **Frontend:** HTML5, CSS3 (Dark Theme responsivo com paleta em laranja/castanho)
- **Banco de Dados:** SQLite3
- **Hospedagem / Deploy:** PythonAnywhere

---

## 📌 Funcionalidades

- **Atrações:** Exibição estruturada dos principais pontos turísticos (Santiago Bernabéu, Palácio Real, Museu do Prado).
- **História e Cultura:** Seções dedicadas à evolução histórica da capital espanhola e à cultura do futebol merengue.
- **Galeria Visual:** Imagens otimizadas com navegação simples e responsiva.

---

## 🚀 Como Executar Localmente

```bash
# Clone o repositório
git clone [https://github.com/pscansantos-art/madrid-experiencias-django.git]

# Entre na pasta
cd madrid-experiencias-django

# Instale as dependências
pip install django

# Execute as migrações
python manage.py migrate

# Inicie o servidor
python manage.py runserver
