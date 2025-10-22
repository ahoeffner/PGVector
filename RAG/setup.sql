
CREATE EXTENSION vector;
CREATE EXTENSION plpython3u;



CREATE OR REPLACE FUNCTION python_version()
  RETURNS VARCHAR
AS $$
    import sys
    return sys.version
$$ LANGUAGE plpython3u;


CREATE OR REPLACE FUNCTION python_path() RETURNS setof text AS $$
    import sys
    return sys.path
$$ LANGUAGE plpython3u;



SELECT version();
SELECT python_version();
SELECT * FROM python_path();


DROP FUNCTION python_path();
DROP FUNCTION python_version();



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


select * from beers;




DROP FUNCTION test;

CREATE OR REPLACE FUNCTION test(text TEXT)
RETURNS REAL[]
LANGUAGE plpython3u
AS $$
	import json
	import base64
	import requests
	
	URL = 'http://host.docker.internal:8000/index'
	
	try:
	    B64_DATA = base64.b64encode(text.encode('utf-8')).decode('utf-8')
	except Exception as e:
	    plpy.error("Error encoding input text to Base64: %s" % str(e))
	    
	data = {'b64': B64_DATA}

	try:
	    r = requests.post(URL, json=data)
	
	    if r.status_code != 200:
	        plpy.error("API call failed. Status: %s, Body: %s" % (r.status_code, r.text))
	
	    response_json = r.json()    
	    chunks = response_json.get('chunks', [])
	
	    if not chunks:
	        plpy.error("API call succeeded but returned no chunks.")
	    
	    embedding = chunks[0].get('embedding')
	
	    if not embedding:
	        plpy.error("Chunk data missing 'embedding' field in the first chunk.")
	
	    return embedding
	
	except requests.exceptions.ConnectionError:
	    plpy.error("ConnectionError: Failed to connect to %s. Ensure the FastAPI service is running" % URL)
	    
	except Exception as e:
	    plpy.error("An unexpected error occurred during API call: %s" % str(e))
	
	return None
$$;


SELECT test('This is the text I want to embed.');











CREATE TABLE documents (
    id BIGSERIAL PRIMARY KEY,
    embedding VECTOR(1536),          -- The column to store the vector embeddings
    content TEXT NOT NULL,           -- The actual text chunk/snippet of your document
    source VARCHAR(255),             -- Path or URL of the original document
    metadata JSONB                   -- Flexible storage for things like page number, title, author, etc.
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

