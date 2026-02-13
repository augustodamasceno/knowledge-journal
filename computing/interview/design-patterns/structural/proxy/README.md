# Proxy Pattern Interview Prep

## Overview
Proxy provides a placeholder to control access to another object, adding behavior such as lazy loading, access control, or logging.

## Theoretical Q&A
1. **What kinds of proxies exist?** Virtual proxies defer expensive initialization, protection proxies enforce permissions, and remote proxies manage network access.
2. **How does Proxy differ from Decorator?** Proxy focuses on controlling access, while Decorator adds responsibilities; proxies often preserve behavior but change timing or scope.
3. **What pitfalls accompany proxies?** Added indirection can hide latency, and excessive proxies may complicate debugging or tracing.

## Practical Exercises
- Extend the sample to track invocation counts for auditing.
- Discuss how exceptions should propagate through a proxy.
- Compare proxy-based lazy loading to initialization-on-demand holder idiom.

### Code Samples
- C++: [cpp/proxy.cpp](cpp/proxy.cpp)
- C#: [csharp/ProxyDemo.cs](csharp/ProxyDemo.cs)
- Java: [java/ProxyDemo.java](java/ProxyDemo.java)
- Python: [python/proxy_demo.py](python/proxy_demo.py)
