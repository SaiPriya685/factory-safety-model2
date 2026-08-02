import sqlite3


DATABASE = "factory.db"


connection = sqlite3.connect(DATABASE)

cursor = connection.cursor()


try:

    cursor.execute(
        """
        ALTER TABLE incidents
        ADD COLUMN evidence_path TEXT
        """
    )

    connection.commit()

    print("evidence_path column added successfully")


except Exception as e:

    print("Migration error:")
    print(e)


finally:

    connection.close()