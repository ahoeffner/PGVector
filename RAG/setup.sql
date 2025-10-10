
CREATE EXTENSION vector;
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



DROP FUNCTION public.setRagData();



CREATE OR REPLACE FUNCTION setRagData()
RETURNS trigger AS $$
	row = TD['new'];
	
	operation = TD['event']
	
	if operation == 'INSERT':
	    row['test'] = f"Value set by Python: INITIAL INSERT"
	    
	elif operation == 'UPDATE':
	    # Example: set a different value for an update
	    row['test'] = f"Value set by Python: UPDATED"
	    
	return 'MODIFY'
$$ LANGUAGE plpython3u;


CREATE OR REPLACE TRIGGER setRagData
BEFORE INSERT OR UPDATE ON test
FOR EACH ROW
EXECUTE FUNCTION setRagData();


insert into test(text) values ('This is a test');
update test set text = 'This is another test'

select * from test;

