steps = [
    [
        ## Data from spotify after getting the playlist
        ## need to save it to attach to accounts
        """
        CREATE TABLE billboard (
            rank SMALLINT NOT NULL,
            title VARCHAR(1000) NOT NULL,
            artist VARCHAR(1000) NOT NULL,
            album_pic VARCHAR(1000) NULL
        );
        """,
        ## Drop the table
        """
        DROP TABLE billboard;
        """,
    ]
]
