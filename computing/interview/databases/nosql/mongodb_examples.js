// ============================================================
// MongoDB — comprehensive examples
// Run with: mongosh shop mongodb_examples.js
//           or paste blocks into mongosh shell
// ============================================================

// ── Switch / create database ──────────────────────────────────
use("shop");

// ── Collections setup ────────────────────────────────────────
db.products.drop();
db.orders.drop();
db.customers.drop();

// ── INSERT ────────────────────────────────────────────────────
db.products.insertMany([
  {
    sku: "HDX-100",
    name: "Wireless Headphones",
    price: 79.99,
    stock: 200,
    category: "electronics",
    tags: ["audio", "bluetooth", "wireless"],
    specs: { driver: "40mm", impedance: 32, weight_g: 250 },
    ratings: []
  },
  {
    sku: "CAB-001",
    name: "USB-C Cable 1m",
    price: 9.99,
    stock: 500,
    category: "accessories",
    tags: ["cable", "usb-c"]
  },
  {
    sku: "BK-ALGO",
    name: "Introduction to Algorithms (CLRS)",
    price: 59.99,
    stock: 80,
    category: "books",
    tags: ["computer-science", "algorithms"]
  }
]);

db.customers.insertMany([
  { _id: 1, name: "Alice", email: "alice@example.com", city: "New York",
    addresses: [{ type: "home", street: "123 Main St", zip: "10001" }] },
  { _id: 2, name: "Bob",   email: "bob@example.com",   city: "Austin" }
]);

// ── FIND (Read) ───────────────────────────────────────────────

// Simple equality filter
db.products.find({ category: "electronics" });

// Comparison operators: $lt, $lte, $gt, $gte, $ne, $eq
db.products.find({ price: { $lt: 50 } });
db.products.find({ price: { $gte: 10, $lte: 100 } });

// Multiple conditions (implicit AND)
db.products.find({ category: "electronics", price: { $lt: 100 } });

// Logical operators
db.products.find({ $or: [{ category: "books" }, { price: { $lt: 15 } }] });
db.products.find({ $and: [{ stock: { $gt: 0 } }, { price: { $lt: 100 } }] });

// Array operators
db.products.find({ tags: "bluetooth" });                         // array contains value
db.products.find({ tags: { $in: ["bluetooth", "usb-c"] } });    // any of
db.products.find({ tags: { $all: ["audio", "wireless"] } });    // all of

// Nested field (dot notation)
db.products.find({ "specs.driver": "40mm" });

// Projection — include / exclude fields
db.products.find({}, { name: 1, price: 1, _id: 0 });

// Sort, limit, skip (pagination)
db.products.find().sort({ price: -1 }).limit(10).skip(0);

// Count
db.products.countDocuments({ category: "electronics" });

// Distinct values
db.products.distinct("category");

// ── UPDATE ────────────────────────────────────────────────────

// $set: update a field
db.products.updateOne(
  { sku: "CAB-001" },
  { $set: { price: 11.99 } }
);

// $inc: increment a numeric field
db.products.updateOne(
  { sku: "HDX-100" },
  { $inc: { stock: -1 } }
);

// $push: append to an array
db.products.updateOne(
  { sku: "HDX-100" },
  { $push: { tags: "premium" } }
);

// $addToSet: append only if not already present
db.products.updateOne(
  { sku: "HDX-100" },
  { $addToSet: { tags: "audio" } }
);

// $pull: remove from array
db.products.updateOne(
  { sku: "HDX-100" },
  { $pull: { tags: "premium" } }
);

// Update many
db.products.updateMany(
  { stock: { $lt: 10 } },
  { $set: { low_stock: true } }
);

// Upsert: insert if not found
db.products.updateOne(
  { sku: "NEW-001" },
  { $set: { name: "New Product", price: 29.99, stock: 100 } },
  { upsert: true }
);

// $unset: remove a field
db.products.updateOne({ sku: "NEW-001" }, { $unset: { low_stock: "" } });

// ── DELETE ────────────────────────────────────────────────────
db.products.deleteOne({ sku: "NEW-001" });
db.products.deleteMany({ stock: 0 });

// ── AGGREGATION PIPELINE ─────────────────────────────────────
// Each stage transforms the documents flowing through it.

// Stage reference:
// $match    → filter (like WHERE)
// $project  → reshape / compute fields (like SELECT)
// $group    → aggregate (like GROUP BY)
// $sort     → sort results
// $limit    → take N results
// $skip     → skip N results
// $unwind   → flatten an array field into separate documents
// $lookup   → left outer join another collection
// $addFields → add computed fields without removing existing ones
// $facet    → multiple pipelines in one pass (for analytics)

// Revenue per category
db.orders.aggregate([
  { $match: { status: { $ne: "cancelled" } } },
  { $unwind: "$items" },
  { $group: {
    _id: "$items.category",
    total_revenue: { $sum: { $multiply: ["$items.qty", "$items.price"] } },
    total_units:   { $sum: "$items.qty" }
  }},
  { $sort: { total_revenue: -1 } }
]);

// $lookup — join products into order items
db.orders.aggregate([
  { $unwind: "$items" },
  { $lookup: {
    from:         "products",
    localField:   "items.product_sku",
    foreignField: "sku",
    as:           "product_info"
  }},
  { $unwind: "$product_info" },
  { $project: {
    order_id: 1,
    product:  "$product_info.name",
    qty:      "$items.qty",
    revenue:  { $multiply: ["$items.qty", "$product_info.price"] }
  }}
]);

// $facet — multi-faceted analytics in one round trip
db.products.aggregate([
  { $facet: {
    by_category: [
      { $group: { _id: "$category", count: { $sum: 1 }, avg_price: { $avg: "$price" } } }
    ],
    price_buckets: [
      { $bucket: {
        groupBy: "$price",
        boundaries: [0, 25, 75, 200, 2000],
        default: "other",
        output: { count: { $sum: 1 } }
      }}
    ]
  }}
]);

// ── INDEXES (MongoDB) ─────────────────────────────────────────
db.products.createIndex({ category: 1, price: -1 });          // compound
db.products.createIndex({ name: "text", description: "text" }); // full-text
db.products.createIndex({ email: 1 }, { unique: true });        // unique
db.products.createIndex({ createdAt: 1 }, { expireAfterSeconds: 3600 }); // TTL

// View all indexes
db.products.getIndexes();

// Explain a query
db.products.find({ category: "electronics" }).explain("executionStats");

// ── TRANSACTIONS (MongoDB 4+, replica set / sharded cluster) ──
// Python-style pseudocode (mongosh uses similar API)
/*
const session = db.getMongo().startSession();
session.startTransaction();
try {
  session.getDatabase("shop").products.updateOne(
    { sku: "HDX-100" }, { $inc: { stock: -1 } }, { session }
  );
  session.getDatabase("shop").orders.insertOne(
    { customer_id: 1, items: [...], status: "pending" }, { session }
  );
  session.commitTransaction();
} catch (e) {
  session.abortTransaction();
} finally {
  session.endSession();
}
*/
