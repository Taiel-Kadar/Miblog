### Technologies
- Python 3.8.2
- Django
- Bootstrap4
- CKeditor
- Taggit
- Heroku
- Gunicorn
- PostgreSQL

### Features
- Create, edit, delete posts.
- Add tags to posts.
- Filter posts by tags.
- Rich text editor.
- Pagination.
- User authentication, login, logout, register.
- Share posts via email.
- Recommend similar posts based on tags.
- Add comments.
- Search Bar

### Installation
- Clone the repository:
  - `git clone https://github.com/Taiel-Kadar/Miblog.git` 
  ![gitclo1ne](https://user-images.githubusercontent.com/51141143/91521375-d94f1600-e8cd-11ea-8af8-1aa9da8a3e44.jpg)
  
- Create virtual environment:
  - `python3 -m venv "venv_name"
  `![createenv](https://user-images.githubusercontent.com/51141143/91521389-e0762400-e8cd-11ea-97cb-6ff71d5f3ac2.jpg)
  
- Activate venv (on Windows replace "/bin/" for "/Scripts/"):
  - `source "venv_name"/bin/activate`
  ![actienv](https://user-images.githubusercontent.com/51141143/91521396-e3711480-e8cd-11ea-88f8-f487b725c9af.jpg)
  
- Install packages:
  - `pip install -r requirements.txt`
  ![pipinstallrequirem](https://user-images.githubusercontent.com/51141143/91521410-ee2ba980-e8cd-11ea-8b66-a4c46e875225.jpg)
  
- Migrate database:
  - `python manage.py migrate`
  ![migrate11](https://user-images.githubusercontent.com/51141143/91521416-f388f400-e8cd-11ea-806a-7d083338d77a.jpg)
  ![migrate22](https://user-images.githubusercontent.com/51141143/91521420-f5eb4e00-e8cd-11ea-8fd6-fe5403e25285.jpg)
  
- Create superuser:
  - `python manage.py createsuperuser`
  ![createsuperuser](https://user-images.githubusercontent.com/51141143/91521428-f97ed500-e8cd-11ea-91f4-c60a50137239.jpg)
  
- Run the server:
  - `python manage.py runserver`
  ![runserver2](https://user-images.githubusercontent.com/51141143/91521435-fc79c580-e8cd-11ea-8372-13f8750f6afa.jpg)
  
- Open the development server, login with the admin account or create a new one.
