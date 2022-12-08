steps = [
    [
        ## Data from spotify after getting the playlist
        ## need to save it to attach to accounts
        """
        CREATE TABLE playlists (
            id SERIAL PRIMARY KEY NOT NULL,
            user_id SMALLINT NOT NULL,
            search_term VARCHAR(1000) NOT NULL,
            playlist_id VARCHAR(1000) NOT NULL UNIQUE,
            name VARCHAR(1000) NOT NULL,
            pic VARCHAR(1000) NOT NULL,
            url VARCHAR(1000) NOT NULL,
            rating SMALLINT NULL
        );
        """,
        ## Drop the table
        """
        DROP TABLE playlists;
        """,
    ]
]
