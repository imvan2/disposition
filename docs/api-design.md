 ### Get a playlist

* Endpoint path: /vibecheck/playlists/
* Endpoint method: GET

* Headers:
  * “X-RapidAPI-Key”: api key,
        “X-RapidAPI-Host”: “spotify23.p.rapidapi.com”
  

* Response: A list of playlists
* Response = requests.request(“GET”, url, headers=headers, params=querystring)
* Response shape:
    ```json
    {
      "playlist": [
        {
          "artist_names": string,
          "artist_ids": string,

          "album_title": string,
          "albumcover_url": string,
          "album_id": string,

          "song_name": string,
          "song_id": string,

          "genre": string,

          "preview_url": string,   
          "sample_uri": string,
        }
      ]
    }
    ```


* Endpoint path: /home/
* Endpoint method: GET

* Headers:
  * “X-RapidAPI-Key”: api key,
        “X-RapidAPI-Host”: “spotify23.p.rapidapi.com”


* Response: A list of top 100 songs from Billboard 
* Response = requests.request(“GET”, url, headers=headers, params=querystring)
* Response shape:
    ```json
    {
      "playlist": [
        {
          "artist_names": string,
          "artist_ids": string,

          "album_title": string,
          "albumcover_url": string,
          "album_id": string,

          "song_name": string,
          "song_id": string,

          "preview_url": string,   
          "sample_uri": string,
        }
      ]
    }
    ```


* Endpoint path: /login/
* Endpoint method: POST 



* Response: Process a user login
* Response = requests.request(“POST”, url, headers=headers, params=querystring)
* Response shape:
    ```json
        {
          "username": string,
          "password": string,
        }
    ```




  * Endpoint path: /personalitytest/
* Endpoint method: POST


* Response: A list of user outputs based on questions provided
* Response = requests.request(POST”, url, headers=headers, params=querystring)
* Response shape:
    ```json
        {

    "mood": chill,
    "activity": staying home
    "beverage": tea
    "button": true
}
```


* Endpoint path: user/playlists/
* Endpoint method: GET


* Response: A list of playlists corresponding to each UserID based off user history
* Response = requests.request(“GET”, url, headers=headers, params=querystring)
* Response shape:
    ```json
    {
      "playlists": [
        {
          "playlist": playlist_id,
        }
      ]
    }
    ```


    
* Endpoint path: /createplaylist/
* Endpoint method: POST


* Response: Once we gotten this playlist, we send a post request to our api
* Response = requests.request(“POST”, url, headers=headers, params=querystring)
* Response shape:
    ```json

        {
          "playlist": playlistid,
        }

    ```


    
