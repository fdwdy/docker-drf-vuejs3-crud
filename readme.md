<h1>Django Rest Framework Vuejs3 Postgresql Docker-Compose CRUD Example App</h1><br/>

<h3>Start:</h3><br/>
clone repo
cd shipments<br/>
docker compose build<br/>
docker compose up<br/>

Open http://localhost:8080<br/>
Add -> Create new Shipment<br/>
Home Page -> Choose shipment in list -> Click edit -> Update or Delete Shipment<br/>

<h3>Run On Host:</h3><br/>
clone repo
cd backend<br/>
create venv<br/>
pip install -r requirements.txt<br/>
python manage.py makemigrations<br/>
python manage.py migrate<br/>
python manage.py runserver 0.0.0.0:8002 --settings=config.settings<br/>
cd client<br/>
npm install<br/>
npm run dev<br/>

<h5>Database:</h5><br/>
PostgreSQL<br/>
<h5>Backend:</h5><br/>
Django Rest Framework<br/>
<h5>Frontend:</h5> <br/>
Vuejs3 Vite Vuelidate Nightwatch.js<br/>
