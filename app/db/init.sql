CREATE TABLE users (
    id BIGINT IDENTITY(1,1) PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    role VARCHAR(10) NOT NULL CHECK (role IN ('client', 'expert')),
    created_at DATETIMEOFFSET DEFAULT SYSDATETIMEOFFSET()
);

CREATE TABLE conversations (
    id BIGINT IDENTITY(1,1) PRIMARY KEY,
    client_id BIGINT NOT NULL,
    expert_id BIGINT NOT NULL,
    last_message_at DATETIMEOFFSET DEFAULT SYSDATETIMEOFFSET(),
    created_at DATETIMEOFFSET DEFAULT SYSDATETIMEOFFSET(),
    FOREIGN KEY (client_id) REFERENCES users(id),
    FOREIGN KEY (expert_id) REFERENCES users(id),
    CONSTRAINT unique_conversation UNIQUE (client_id, expert_id)
);

CREATE TABLE conversation_reads (
    user_id BIGINT NOT NULL,
    conversation_id BIGINT NOT NULL,
    last_read_at DATETIMEOFFSET DEFAULT SYSDATETIMEOFFSET(),
    PRIMARY KEY (user_id, conversation_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (conversation_id) REFERENCES conversations(id)
);

CREATE TABLE messages (
    id BIGINT IDENTITY(1,1) PRIMARY KEY,
    conversation_id BIGINT NOT NULL,
    sender_id BIGINT NOT NULL,
    message TEXT NOT NULL,
    sent_at DATETIMEOFFSET DEFAULT SYSDATETIMEOFFSET(),
    FOREIGN KEY (conversation_id) REFERENCES conversations(id),
    FOREIGN KEY (sender_id) REFERENCES users(id)
);