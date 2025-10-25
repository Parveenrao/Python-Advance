# Sql Achemy

"""SQLAlchemy is widely considered the best ORM in Python because it gives the flexibility of both an ORM and a Core layer, 
    making it suitable for both simple and highly complex queries. It is database-agnostic, supports clean migrations through Alembic, 
    and provides strong performance optimizations like lazy/eager loading. Its mature ecosystem and community support
    make it a production-grade choice for scalable applications
    """
    
    
""" It has two layers:

SQLAlchemy Core → gives you raw SQL power with Pythonic abstraction.

SQLAlchemy ORM → lets you map Python classes to database tables and query like objects.

You can mix both (ORM for common queries, Core for complex queries). Most ORMs don't give this dual power.   """

"""
Works with all major databases (PostgreSQL, MySQL, SQLite, Oracle, MSSQL).

If you switch from SQLite (for dev) → PostgreSQL (for prod), just change the connection string, no major code rewrite. 
"""