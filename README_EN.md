
# Django API Project

## Project Overview
This project provides an API server using Django and a deep learning model to upload `.png` files and determine whether the uploaded image is AI-generated.

---

## 1. Virtual Environment Creation and Activation

### Creating a Virtual Environment
1. Create a project directory and navigate to it:
   ```bash
   mkdir my_django_project
   cd my_django_project
   ```

2. Create a Python virtual environment:
   ```bash
   python -m venv venv
   ```

### Activating the Virtual Environment
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

---

## 2. Installing Required Modules

### Starting a New Project
1. With the virtual environment activated, install Django and the necessary modules:
   ```bash
   pip install django djangorestframework pillow
   ```

2. Save the installed modules to a `requirements.txt` file:
   ```bash
   pip freeze > requirements.txt
   ```

### For an Existing Project or When `requirements.txt` is Provided
1. With the virtual environment activated, run the following command:
   ```bash
   pip install -r requirements.txt
   ```

---

## 3. Running the Server
1. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

2. Verify that the server is running by visiting `http://127.0.0.1:8000/api/image/` in a browser.

---

## 4. API Testing Instructions

### Installing Postman
1. Download and install Postman from the [Postman Download Page](https://www.postman.com/downloads/).

### Testing the API
1. Open Postman and create a new request.
2. Set the **Method** to `POST`.
3. Enter the **URL**: `http://127.0.0.1:8000/api/image/`.
4. In the Body tab, select `form-data`:
   - Key: `multipartFile`
   - Type: `File`
   - Value: Upload a `.png` file.
5. Click the `Send` button to send the request.

### Response Examples
#### Success:
```json
{
    "suspiciousness": 0.9
}
```

#### Failure:
1. If no file is provided:
   ```json
   {
       "error": "No file provided."
   }
   ```

2. If the file format is not `.png`:
   ```json
   {
       "error": "Only .png files are supported."
   }
   ```

---
