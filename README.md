# ControleEstoque
https://www.youtube.com/watch?v=nlHfCt0HuGY&list=PLsGCdfxkV9uqj9DwI6Y72JyvXeA-9mAjc&index=6

### Como rodar o projeto?
Clone esse repositório.
Crie um virtualenv com Python 3.
Ative o virtualenv.
Instale as dependências.
Rode as migrações.

git clone git@github.com:cstoski/ControleEstoque.git
cd estoque
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver