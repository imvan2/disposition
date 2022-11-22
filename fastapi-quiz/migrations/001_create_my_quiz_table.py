steps = [
    [
        ## Data from quiz from user
        """
        CREATE TABLE quiz_answer (
            id SERIAL PRIMARY KEY NOT NULL,
            user_id SMALLINT NOT NULL,
            q_number SMALLINT NOT NULL UNIQUE,
            question VARCHAR(1000) NOT NULL,
            answer VARCHAR(50) NOT NULL,
            value SMALLINT NOT NULL
        );
        """,
        ## Drop the table
        """
        DROP TABLE quiz_answer;
        """
    ],
    [
        ## Let the team create question and answers
        """
        CREATE TABLE quiz_question_answer (
            id SERIAL PRIMARY KEY NOT NULL,
            q_number SMALLINT NOT NULL UNIQUE,
            question VARCHAR(1000) NOT NULL,
            answer1 VARCHAR(50) NOT NULL,
            answer2 VARCHAR(50) NOT NULL,
            answer3 VARCHAR(50) NOT NULL,
            answer4 VARCHAR(50) NOT NULL,
            value1 SMALLINT NOT NULL,
            value2 SMALLINT NOT NULL,
            value3 SMALLINT NOT NULL,
            value4 SMALLINT NOT NULL
        );
        """,
        ## Drop the table
        """
        DROP TABLE quiz_question_answer;
        """
    ]

]
