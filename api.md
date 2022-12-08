# APIs

## Accounts
- Methods: `POST`, `GET`, `DELETE`, `PUT`


### Creating an account, `POST`, /signup
Input:
```
{
  "first_name": "John",
  "last_name": "Smith",
  "username": "jsmith",
  "password": "password123,
  "email": "jsmith@gmail.com
}
```

Output:
```
{
  "first_name": "John",
  "last_name": "Smith",
  "username": "jsmith",
  "password": "password123,
  "email": "jsmith@gmail.com
}
```
### Getting one account, `GET`, /accounts/{username}
Input:
```
{
  "username": "jsmith"
}
```

Output:
```
{
  "id": 1,
  "first_name": "john",
  "last_name": "smith",
  "username": "jsmith",
  "hashed_password": "<hashed_password>",
  "email": "jsmith"
}

```

### Updating an account, `PUT`, /accounts/{id}

Parameter: "id": 1

Input:
```
{
  "first_name": "Bob",
  "last_name": "Name",
  "username": "bname",
  "password": "password123,
  "email": "bname@gmail.com
}
```

Output:
```
{
  "first_name": "Bob",
  "last_name": "Name",
  "username": "bname",
  "password": "password123,
  "email": "bname@gmail.com
}
```

### Deleting an account, `DELETE`, /accounts/{id}

Parameter: "id": 1

Ouput:
```
{
  true
}
```


## Quiz
- Methods: `POST`, `GET`

### Creating an quiz result, `POST`, /answers
Input:
```
{
  "user_id": ,
  "mood": "gloomy",
  "genre": "jazz"
}
```
Output:
```
{
  "id": 1,
  "user_id": 1,
  "mood": "gloomy",
  "genre": "jazz"
}
```

### Getting all quiz results, `GET` , /answers
Output:
```
[
  {
    "id": 1,
    "user_id": 1,
    "mood": "gloomy",
    "genre": "jazz"
  }
]
```


## Questions
- Methods: `POST`, `GET`

### Creating a question, `POST` , /questions
Input:
```
{
  "q_number": 1,
  "question": "What's your fav food?",
  "answer1": "Sushi",
  "answer2": "Ramen",
  "answer3": "Fried Chicken",
  "answer4": "Salad",
  "value1": 1,
  "value2": 2,
  "value3": 3,
  "value4": 4
}
```
Output:
```
{
  "q_number": 1,
  "question": "What's your fav food?",
  "answer1": "Sushi",
  "answer2": "Ramen",
  "answer3": "Fried Chicken",
  "answer4": "Salad",
  "value1": 1,
  "value2": 2,
  "value3": 3,
  "value4": 4,
  "id": 3
}
```

### Getting all questions, `GET` , /questions
Output:
```
[
  {
    "q_number": 1,
    "question": "What's your fav food?",
    "answer1": "Sushi",
    "answer2": "Ramen",
    "answer3": "Fried Chicken",
    "answer4": "Salad",
    "value1": 1,
    "value2": 2,
    "value3": 3,
    "value4": 4,
    "id": 3
  }
]
```

### Playlists

- Methods: `POST`, `GET`, `DELETE`, `PUT`

### Get a Playlist, `GET` , /playlists/{playlist_id}}
Output:
```
{
  "id": 0,
  "user_id": 0,
  "search_term": "upbeat",
  "playlist_id": "0vvXsWCC9xrXsKd4FyS8kM",
  "name": "lo-fi hiphop",
  "pic": "https://i.scdn.co/image/ab67706c0000bebb171508467d737fe9765b416c",
  "url": "https://open.spotify.com/playlist/0vvXsWCC9xrXsKd4FyS8kM",
  "rating": 5
}
```
### Post  a Playlist, `POST` , /playlists/{playlist_id}}

Input:
```
{
  "user_id": 0,
  "search_term": "upbeat",
  "playlist_id": "0vvXsWCC9xrXsKd4FyS8kM",
  "name": "lo-fi hiphop",
  "pic": "https://i.scdn.co/image/ab67706c0000bebb171508467d737fe9765b416c",
  "url": "https://open.spotify.com/playlist/0vvXsWCC9xrXsKd4FyS8kM",
  "rating": 5
}
```

### Delete a Playlist, `DELETE` , /playlists/{playlist_id}}
Input:
```
"playlist_id": "0vvXsWCC9xrXsKd4FyS8kM"
```

Output:
```
{
  true
}
```

### Update a Playlist, `PUT` , /playlists/{id}}
Input:
```
{
  "user_id": 0,
  "search_term": "upbeat",
  "playlist_id": "0vvXsWCC9xrXsKd4FyS8kM",
  "name": "lo-fi hiphop",
  "pic": "https://i.scdn.co/image/ab67706c0000bebb171508467d737fe9765b416c",
  "url": "https://open.spotify.com/playlist/0vvXsWCC9xrXsKd4FyS8kM",
  "rating": 5
}
```

Output:
```
{
  "id": 0,
  "user_id": 0,
  "search_term": "upbeat",
  "playlist_id": "0vvXsWCC9xrXsKd4FyS8kM",
  "name": "lo-fi hiphop",
  "pic": "https://i.scdn.co/image/ab67706c0000bebb171508467d737fe9765b416c",
  "url": "https://open.spotify.com/playlist/0vvXsWCC9xrXsKd4FyS8kM",
  "rating": 5
}
```
