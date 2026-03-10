// ============================================================
// Neo4j — Cypher examples
// Run in: Neo4j Browser (http://localhost:7474) or cypher-shell
// ============================================================

// ── Clear demo data ──────────────────────────────────────────
MATCH (n) DETACH DELETE n;

// ── Create nodes ──────────────────────────────────────────────
// Node syntax: (variable:Label {property: value})
CREATE (:Person  {id: 1, name: "Alice",  age: 30, city: "New York"})
CREATE (:Person  {id: 2, name: "Bob",    age: 25, city: "Austin"})
CREATE (:Person  {id: 3, name: "Carol",  age: 28, city: "Seattle"})
CREATE (:Person  {id: 4, name: "Dave",   age: 35, city: "New York"})

CREATE (:Product {id: 10, name: "Wireless Headphones", price: 79.99,  category: "electronics"})
CREATE (:Product {id: 11, name: "CLRS Book",           price: 59.99,  category: "books"})
CREATE (:Product {id: 12, name: "USB-C Cable",         price:  9.99,  category: "accessories"})

CREATE (:Category {name: "electronics"})
CREATE (:Category {name: "books"})
CREATE (:Category {name: "accessories"});

// ── Create relationships ──────────────────────────────────────
// Relationship syntax: (a)-[:TYPE {prop: val}]->(b)

// Social graph
MATCH (a:Person {name: "Alice"}), (b:Person {name: "Bob"})
CREATE (a)-[:KNOWS {since: 2018, strength: 0.8}]->(b);

MATCH (a:Person {name: "Alice"}), (c:Person {name: "Carol"})
CREATE (a)-[:KNOWS {since: 2020}]->(c);

MATCH (b:Person {name: "Bob"}), (d:Person {name: "Dave"})
CREATE (b)-[:KNOWS {since: 2021}]->(d);

// Purchases
MATCH (a:Person {name: "Alice"}),   (p:Product {name: "Wireless Headphones"})
CREATE (a)-[:PURCHASED {on: date("2024-01-10"), qty: 1, price_paid: 79.99}]->(p);

MATCH (a:Person {name: "Alice"}),   (p:Product {name: "CLRS Book"})
CREATE (a)-[:PURCHASED {on: date("2024-03-15"), qty: 1, price_paid: 59.99}]->(p);

MATCH (b:Person {name: "Bob"}),     (p:Product {name: "USB-C Cable"})
CREATE (b)-[:PURCHASED {on: date("2024-02-20"), qty: 2, price_paid: 9.99}]->(p);

MATCH (d:Person {name: "Dave"}),    (p:Product {name: "Wireless Headphones"})
CREATE (d)-[:PURCHASED {on: date("2024-02-14"), qty: 1, price_paid: 79.99}]->(p);

// Reviews
MATCH (a:Person {name: "Alice"}), (p:Product {name: "Wireless Headphones"})
CREATE (a)-[:REVIEWED {rating: 5, comment: "Amazing sound!"}]->(p);

// Category membership
MATCH (p:Product), (c:Category) WHERE p.category = c.name
CREATE (p)-[:BELONGS_TO]->(c);

// ── Basic READ ────────────────────────────────────────────────

// All people
MATCH (p:Person) RETURN p.name, p.age ORDER BY p.name;

// Specific node
MATCH (p:Person {name: "Alice"}) RETURN p;

// All relationships from Alice
MATCH (alice:Person {name: "Alice"})-[r]->(other)
RETURN type(r), other.name, properties(r);

// ── PATTERN MATCHING ─────────────────────────────────────────

// Direct friends of Alice
MATCH (alice:Person {name: "Alice"})-[:KNOWS]->(friend:Person)
RETURN friend.name, friend.city;

// Products purchased by Alice
MATCH (alice:Person {name: "Alice"})-[:PURCHASED]->(p:Product)
RETURN p.name, p.price;

// Friends of Alice who also bought what Alice bought (recommendation)
MATCH (alice:Person {name: "Alice"})-[:PURCHASED]->(p:Product)
     <-[:PURCHASED]-(other:Person)
WHERE other.name <> "Alice"
RETURN DISTINCT other.name, COLLECT(p.name) AS common_products;

// ── MULTI-HOP TRAVERSAL ───────────────────────────────────────

// 2 hops: products bought by Alice's friends (not Alice)
MATCH (alice:Person {name: "Alice"})-[:KNOWS]->(friend)-[:PURCHASED]->(p:Product)
RETURN DISTINCT p.name, p.price, COUNT(friend) AS friend_buyers
ORDER BY friend_buyers DESC;

// Variable-length path: friends up to 3 hops away
MATCH (alice:Person {name: "Alice"})-[:KNOWS*1..3]->(connection)
RETURN DISTINCT connection.name;

// ── SHORTEST PATH ─────────────────────────────────────────────
MATCH path = shortestPath(
    (alice:Person {name: "Alice"})-[*]-(dave:Person {name: "Dave"})
)
RETURN [n IN nodes(path) | n.name] AS path_names, length(path) AS hops;

// All shortest paths
MATCH path = allShortestPaths(
    (alice:Person {name: "Alice"})-[:KNOWS*]-(dave:Person {name: "Dave"})
)
RETURN path;

// ── AGGREGATION ───────────────────────────────────────────────

// Purchase count and revenue per product
MATCH (p:Person)-[r:PURCHASED]->(pr:Product)
RETURN pr.name,
       COUNT(p)              AS buyers,
       SUM(r.qty)            AS total_units,
       SUM(r.qty * r.price_paid) AS revenue
ORDER BY revenue DESC;

// Average rating per product
MATCH (p:Person)-[r:REVIEWED]->(pr:Product)
RETURN pr.name,
       ROUND(AVG(r.rating), 2) AS avg_rating,
       COUNT(r)                AS review_count;

// People grouped by city
MATCH (p:Person)
RETURN p.city, COLLECT(p.name) AS residents, COUNT(p) AS count
ORDER BY count DESC;

// ── OPTIONAL MATCH (like LEFT JOIN) ──────────────────────────
MATCH (p:Person)
OPTIONAL MATCH (p)-[:PURCHASED]->(pr:Product)
RETURN p.name, COUNT(pr) AS purchase_count;

// ── WHERE clauses and predicates ─────────────────────────────
MATCH (p:Person)
WHERE p.age > 25 AND p.city IN ["New York", "Austin"]
RETURN p.name, p.age, p.city;

// Relationship property filter
MATCH (a:Person)-[r:KNOWS]->(b:Person)
WHERE r.since < 2020
RETURN a.name, b.name, r.since;

// EXISTS check
MATCH (p:Person)
WHERE EXISTS { MATCH (p)-[:PURCHASED]->(:Product) }
RETURN p.name AS paying_customer;

// ── CREATE / MERGE / UPDATE ───────────────────────────────────

// Pure create (always inserts new node)
CREATE (carol:Person {id: 5, name: "Eve", age: 22, city: "Boston"});

// MERGE: create only if the matching pattern doesn't exist
MERGE (p:Person {name: "Frank"})
ON CREATE SET p.age = 40, p.city = "Chicago", p.created = timestamp()
ON MATCH  SET p.last_seen = timestamp();

// SET: update properties
MATCH (p:Product {name: "CLRS Book"})
SET p.price = 54.99, p.on_sale = true;

// REMOVE: delete a property or label
MATCH (p:Product {name: "CLRS Book"})
REMOVE p.on_sale;

// ── DELETE ────────────────────────────────────────────────────

// Delete a node and all its relationships
MATCH (p:Person {name: "Eve"})
DETACH DELETE p;

// Delete only a relationship (keep nodes)
MATCH (a:Person {name: "Alice"})-[r:KNOWS]->(b:Person {name: "Carol"})
DELETE r;

// ── INDEXES & CONSTRAINTS ─────────────────────────────────────

// Uniqueness constraint (also creates an index)
CREATE CONSTRAINT person_id IF NOT EXISTS
FOR (p:Person) REQUIRE p.id IS UNIQUE;

CREATE CONSTRAINT product_id IF NOT EXISTS
FOR (p:Product) REQUIRE p.id IS UNIQUE;

// Regular index for fast lookups
CREATE INDEX person_name IF NOT EXISTS FOR (p:Person) ON (p.name);
CREATE INDEX product_category IF NOT EXISTS FOR (p:Product) ON (p.category);

// Full-text index
CREATE FULLTEXT INDEX product_search IF NOT EXISTS
FOR (n:Product) ON EACH [n.name];

CALL db.index.fulltext.queryNodes("product_search", "wireless")
YIELD node, score
RETURN node.name, score;

// ── EXPLAIN / PROFILE ─────────────────────────────────────────
EXPLAIN MATCH (p:Person {name: "Alice"})-[:PURCHASED]->(pr:Product)
        RETURN pr.name;

PROFILE MATCH (p:Person {name: "Alice"})-[:PURCHASED]->(pr:Product)
        RETURN pr.name;
