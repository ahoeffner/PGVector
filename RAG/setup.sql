CREATE EXTENSION plpython3u;

CREATE TABLE documents (
    id BIGSERIAL PRIMARY KEY,
    embedding VECTOR(1536),          -- The column to store the vector embeddings
    content TEXT NOT NULL,           -- The actual text chunk/snippet of your document
    source VARCHAR(255),             -- Path or URL of the original document
    metadata JSONB                   -- Flexible storage for things like page number, title, author, etc.
);


CREATE TABLE test(
	id serial primary key,
	text text not null,
	test text
);


DO $$
BEGIN
IF NOT EXISTS (SELECT 1 FROM pg_language WHERE lanname = 'plpython3u') THEN
RAISE EXCEPTION 'PL/Python3U is not installed. Please run CREATE EXTENSION plpython3u;';
END IF;
END
$$ LANGUAGE plpgsql;