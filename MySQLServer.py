try:

    CREATE DATABASE IF NOT EXISTS alx_book_store;

    print("Database 'alx_book_store' created successfully!")

except error as e:
    print("failed to connect to database")

alx_book_store.close()
