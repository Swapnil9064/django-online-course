# Online Course Django Assessment App
Windows setup:
1. Extract ZIP and open CMD in this folder.
2. `python -m venv .venv`
3. `.venv\\Scripts\\activate`
4. `pip install -r requirements.txt`
5. `python manage.py makemigrations`
6. `python manage.py migrate`
7. `python manage.py createsuperuser`
8. `python manage.py runserver`
Open http://127.0.0.1:8000/admin/ and create a Course, Lessons, Questions and Choices. Mark one choice correct for each question. Create a normal user account, log in at /accounts/login/ if configured by your environment or use Django admin account for local testing. The assessment views require login. Review against the course starter/rubric before submitting. GitHub links must point to files you actually upload; screenshots must be captured from the running app.
