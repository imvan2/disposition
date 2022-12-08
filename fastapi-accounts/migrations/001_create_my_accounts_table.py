steps = [
    [
        ## Create the table
        """
        CREATE TABLE accounts (
            id SERIAL PRIMARY KEY NOT NULL,
            first_name VARCHAR(1000) NOT NULL,
            last_name VARCHAR(1000) NOT NULL,
            username VARCHAR(1000) NOT NULL,
            hashed_password VARCHAR(1000) NOT NULL,
            email VARCHAR(1000) NOT NULL
        );
        """,
        ## Drop the table
        """
        DROP TABLE accounts;
        """,
    ]
]
