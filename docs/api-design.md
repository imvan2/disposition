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


    
