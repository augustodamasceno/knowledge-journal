#!/usr/bin/env bash
# ============================================================
# Redis — comprehensive examples
# Run: redis-cli < redis_examples.sh
#      or paste blocks into: redis-cli
# ============================================================

# ── Strings ───────────────────────────────────────────────────
SET user:1001:name "Alice"
GET user:1001:name                     # "Alice"

# SET with expiry (seconds)
SETEX session:abc123 3600 "user_id=1001"
TTL  session:abc123                    # seconds remaining

# SET with options (NX = only if not exists, XX = only if exists)
SET inventory:42 200 NX                # create if absent
SET inventory:42 199 XX                # update if present

# Atomic counters
INCR  page_views:home
INCRBY likes:post:99  5
DECR  inventory:42
DECRBY inventory:42 10

# Append / string length
APPEND log:events "event1\n"
STRLEN user:1001:name

# ── Hashes (field-value map for an object) ────────────────────
HSET product:42 name "Wireless Headphones" price 79.99 stock 150 category electronics
HGET product:42 price                   # "79.99"
HMGET product:42 name price             # ["Wireless Headphones", "79.99"]
HGETALL product:42
HINCRBY product:42 stock -1
HKEYS   product:42
HVALS   product:42
HLEN    product:42
HDEL    product:42 category
HEXISTS product:42 name                 # 1

# ── Lists (ordered, duplicates allowed) ───────────────────────
# RPUSH = push to tail; LPUSH = push to head
RPUSH task_queue "job:1" "job:2" "job:3"
LPUSH priority_queue "urgent:1"

LPOP  task_queue                        # dequeue from front -> "job:1"
RPOP  task_queue                        # dequeue from tail  -> "job:3"
LLEN  task_queue                        # 1
LRANGE task_queue 0 -1                  # all elements
LINDEX task_queue 0                     # element at index 0
LINSERT task_queue BEFORE "job:2" "job:1.5"

# Blocking pop (useful for worker queues): waits up to 5 seconds
BLPOP task_queue 5

# Trim to keep only last 1000 elements
LTRIM recent_actions 0 999

# ── Sets (unordered, unique) ─────────────────────────────────
SADD online_users user:1 user:2 user:3
SISMEMBER online_users user:2           # 1
SMEMBERS  online_users
SCARD     online_users                  # count
SREM      online_users user:3

# Set operations
SADD premium_users user:1 user:4
SINTER  online_users premium_users     # intersection: {user:1}
SUNION  online_users premium_users     # union: {user:1, user:2, user:4}
SDIFF   online_users premium_users     # difference: {user:2}

# Store result of operation in a new set
SINTERSTORE vip_online online_users premium_users

# Random member
SRANDMEMBER online_users 2             # 2 random members

# ── Sorted Sets (score-based ranking) ────────────────────────
ZADD leaderboard 1500 "alice"
ZADD leaderboard 2300 "bob"
ZADD leaderboard  900 "carol"
ZADD leaderboard 1800 "dave"

ZSCORE   leaderboard "alice"           # 1500
ZRANK    leaderboard "alice"           # rank (0-based, ascending)
ZREVRANK leaderboard "alice"           # rank (0-based, descending)

# Top 3 players (highest score first)
ZREVRANGE leaderboard 0 2 WITHSCORES

# Players with scores between 1000 and 2000
ZRANGEBYSCORE leaderboard 1000 2000 WITHSCORES

ZINCRBY leaderboard 200 "alice"        # alice's score: 1700
ZREM    leaderboard "carol"            # remove a member
ZCARD   leaderboard                    # count

# ── Bitmaps ───────────────────────────────────────────────────
# Track daily active users (each bit = one user ID)
SETBIT  dau:2024-03-20 1001 1          # user 1001 was active
SETBIT  dau:2024-03-20 1002 1
GETBIT  dau:2024-03-20 1001            # 1
BITCOUNT dau:2024-03-20                # total active users

# Bitwise AND / OR across days (weekly active users)
BITOP OR  wau:2024-W12 dau:2024-03-18 dau:2024-03-19 dau:2024-03-20

# ── HyperLogLog (approximate cardinality) ────────────────────
PFADD  uv:page:/home user:1 user:2 user:3 user:1    # user:1 counted once
PFCOUNT uv:page:/home                               # ≈ 3 (may have slight error)
PFMERGE uv:site uv:page:/home uv:page:/about        # merge multiple HLLs

# ── Pub/Sub ───────────────────────────────────────────────────
# In one terminal:
# SUBSCRIBE notifications
# In another:
PUBLISH notifications "order:shipped:9981"
PUBLISH notifications "order:delivered:9980"

# Pattern subscribe
# PSUBSCRIBE order:*

# ── Streams (append-only log, like Kafka) ────────────────────
# * means auto-generate ID (timestamp-sequence)
XADD events * type "order_placed" order_id "9982" customer "alice"
XADD events * type "payment_received" order_id "9982" amount "79.99"

XLEN    events
XRANGE  events - +                     # all entries
XREAD COUNT 10 STREAMS events 0-0     # read from beginning

# Consumer groups (enables competing consumers)
XGROUP CREATE events order-workers $ MKSTREAM
XREADGROUP GROUP order-workers worker-1 COUNT 5 STREAMS events >
XACK events order-workers 1711234567890-0   # acknowledge processed

# ── Key management ────────────────────────────────────────────
EXPIRE  user:1001:name 86400           # TTL 1 day
PEXPIRE session:abc123 300000          # TTL in milliseconds
PERSIST user:1001:name                 # remove TTL
TTL     user:1001:name                 # -1 = no expiry, -2 = key not found

# Key patterns
KEYS    user:*                         # all user keys (avoid in production)
SCAN    0 MATCH "user:*" COUNT 100    # cursor-based, production-safe
TYPE    product:42                     # hash
OBJECT  ENCODING product:42            # ziplist or hashtable

DEL  product:42                        # synchronous delete
UNLINK product:42                      # async delete (non-blocking)

# ── Transactions ──────────────────────────────────────────────
MULTI
  INCR  order_counter
  RPUSH order_log "order:9983"
EXEC

# DISCARD cancels a queued transaction
MULTI
  SET foo bar
DISCARD

# Optimistic locking with WATCH
# WATCH key: if key changes between WATCH and EXEC, MULTI/EXEC returns nil
WATCH inventory:42
MULTI
  DECR inventory:42
EXEC    # nil if inventory:42 was modified concurrently -> retry

# ── Server info ───────────────────────────────────────────────
INFO server
INFO memory
INFO stats
DBSIZE                                 # number of keys in current DB
CONFIG GET maxmemory
CONFIG SET maxmemory-policy allkeys-lru
