# Covid19 ETL

> Short description of what this project does. *(Optional, fill this in later)*

## 🛠️ Setup Instructions

Follow these steps to set up and run this project locally.

---

### 1. Create a Virtual Environment

```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

* **Windows:**

```bash
venv\Scripts\activate
```

* **MacOS/Linux:**

```bash
source venv/bin/activate
```

---

### 3. Install Required Packages

```bash
pip install python-dotenv pandas numpy seaborn
```

---

### 4. Freeze Dependencies

```bash
pip freeze > requirements.txt
```

---

### 5. Set Up Environment Variables

* Create a `.env` file in the root directory:

```bash
touch .env
```

* Add your database credentials and any other secrets to the file:

```
DB_HOST=your_db_host
DB_USER=your_db_user
DB_PASSWORD=your_db_password
...
```

---

### 6. Create `.gitignore`

Make sure to ignore sensitive or unnecessary files by adding the following to `.gitignore`:

```
.env
venv/
```

---

## ▶️ Running the Project

To run the project on a new machine:

1. Create and activate a virtual environment
2. Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

### 🧪 Optional: Use Poetry

If you prefer using [Poetry](https://python-poetry.org/):

```bash
poetry install
```

---

## ✅ Notes

* Ensure that your `.env` file is **never committed** to version control.
* Always activate your virtual environment before running or developing.
* Keep your `requirements.txt` updated when adding new packages.

