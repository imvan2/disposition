steps = [
    [
        ## Data from spotify after getting the playlist
        ## need to save it to attach to accounts
        """
        CREATE TABLE billboard (
            id SERIAL PRIMARY KEY NOT NULL,
            rank SMALLINT NOT NULL,
            title VARCHAR(1000) NOT NULL,
            artist VARCHAR(1000) NOT NULL UNIQUE,
            album VARCHAR(1000) NOT NULL
        );
        """,
        ## Drop the table
        """
        DROP TABLE billboard;
        """,
    ]
]
