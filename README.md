# Epam Devops Task

App built with Python to solve 3 katas. I combined them into a small Flask application and exposed some endpoints where parameters can be sent in the body in JSON format.

It has unit testing with pytest and also it's dockerized to just plug and play in any server

## Instructions to Run and Deploy the App

To build and run the app using Docker Compose, execute the following command:

```bash
docker compose up -d --build
```

# API Documentation

## 1. **`/costs`**

**Method:** `POST`  
**Description:** Calculates the total cost of selected items, including an additional tax.

### Request Body (JSON):

```json
{
  "items": ["socks", "sweater"],
  "tax": 0.1
}
```

## 2. **`/concatenate`**

**Method:** `POST`  
**Description:** Concatenates a list of words into a single string taking one letter of each word based on the position in the array.

### Request Body (JSON):

```json
{
  "words": ["hello", "world"]
}
```

## 3. **`/dictionary/newentry`**

**Method:** `POST`  
**Description:** Adds a new word and its description to the dictionary.

### Request Body (JSON):

```json
{
  "word": "python",
  "description": "A high-level programming language."
}
```

## 4. **`/dictionary/look`**

**Method:** `GET`  
**Description:** Looks up the description of a word in the dictionary.

### Query Parameters:

- **`word`** (required): The word to look up in the dictionary.

### Example Request:

GET /dictionary/look?word=python
