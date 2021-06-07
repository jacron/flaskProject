#cd /Users/orion/Dev/klanten/wur/flaskProject || exit
python=/Users/orion/.virtualenvs/venv/flaskProject/bin/python
export FLASK_APP=app.py
export FLASK_ENV=development
export FLASK_DEBUG=0
$python -m flask run
