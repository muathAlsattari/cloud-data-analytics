from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID

schema = Schema(title=ID(stored=True), content=TEXT)
ix = create_in("indexdir", schema)

writer = ix.writer()
writer.add_document(title="Doc1", content="Artificial Intelligence Research")
writer.commit()

# Query
from whoosh.qparser import QueryParser
with ix.searcher() as searcher:
    q = QueryParser("content", ix.schema).parse("intelligence")
    results = searcher.search(q)
    print(results[0].highlights("content"))
