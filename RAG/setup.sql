
CREATE EXTENSION vector;
CREATE EXTENSION plpython3u;

DROP TABLE beers;


CREATE TABLE beers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    style VARCHAR(255),
    brewery VARCHAR(255),
    beer_name_full VARCHAR(255),
    description TEXT,
    abv NUMERIC(4, 2),        -- Alkoholprocent
    min_ibu INTEGER,          -- IBU er et heltal
    max_ibu INTEGER,
    astringency NUMERIC,
    body NUMERIC,
    alcohol NUMERIC,
    bitter NUMERIC,
    sweet NUMERIC,
    sour NUMERIC,
    salty NUMERIC,
    fruits NUMERIC,
    hoppy NUMERIC,
    spices NUMERIC,
    malty NUMERIC,
    review_aroma NUMERIC,
    review_appearance NUMERIC,
    review_palate NUMERIC,
    review_taste NUMERIC,
    review_overall NUMERIC,
    number_of_reviews INTEGER
);

# Run copy from prompt
# \COPY beers (name, style, brewery, beer_name_full, description, abv, min_ibu, max_ibu, astringency, body, alcohol, bitter, sweet, sour, salty, fruits, hoppy, spices, malty, review_aroma, review_appearance, review_palate, review_taste, review_overall, number_of_reviews) FROM '/host/beer_profile_and_ratings.csv' WITH (FORMAT CSV, HEADER TRUE, DELIMITER ',');

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

