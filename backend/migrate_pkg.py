"""One-time migration: add pkg column and copy description -> pkg."""
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "longkitech.db"


def migrate():
    conn = sqlite3.connect(str(DB_PATH))
    cur = conn.cursor()

    # Check if pkg column already exists
    cur.execute("PRAGMA table_info(products)")
    cols = [row[1] for row in cur.fetchall()]
    if "pkg" in cols:
        print("pkg column already exists, skipping add.")
    else:
        cur.execute("ALTER TABLE products ADD COLUMN pkg VARCHAR(200)")
        print("Added pkg column.")

    # Copy description -> pkg where pkg is empty
    cur.execute("UPDATE products SET pkg = description WHERE pkg IS NULL OR pkg = ''")
    conn.commit()
    affected = cur.rowcount
    print(f"Copied description to pkg for {affected} rows.")

    # Verify
    cur.execute("SELECT COUNT(*) FROM products WHERE pkg IS NOT NULL AND pkg != ''")
    count = cur.fetchone()[0]
    print(f"Total products with pkg set: {count}")

    conn.close()
    print("Migration complete.")


if __name__ == "__main__":
    migrate()
