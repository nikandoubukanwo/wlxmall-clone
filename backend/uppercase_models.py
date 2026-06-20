"""Convert all model numbers in the products table to uppercase."""
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "longkitech.db"


def uppercase_models():
    conn = sqlite3.connect(str(DB_PATH))
    cur = conn.cursor()

    # Check how many are not already uppercase
    cur.execute("SELECT COUNT(*) FROM products WHERE model != UPPER(model)")
    total = cur.fetchone()[0]
    print(f"Found {total} products with non-uppercase model numbers.")

    if total == 0:
        print("All model numbers are already uppercase.")
        conn.close()
        return

    # Preview a few
    cur.execute("SELECT id, model FROM products WHERE model != UPPER(model) LIMIT 5")
    print("\nSample rows to be updated:")
    for row in cur:
        print(f"  [{row[0]}] '{row[1]}' -> '{row[1].upper()}'")

    # Do the update
    cur.execute("UPDATE products SET model = UPPER(model) WHERE model != UPPER(model)")
    conn.commit()
    affected = cur.rowcount
    print(f"\nUpdated {affected} rows.")

    # Also uppercase the name field (which mirrors model)
    cur.execute("UPDATE products SET name = UPPER(name) WHERE name != UPPER(name)")
    conn.commit()
    print(f"Updated {cur.rowcount} rows for name field.")

    # Verify
    cur.execute("SELECT COUNT(*) FROM products WHERE model != UPPER(model)")
    remaining = cur.fetchone()[0]
    print(f"Remaining non-uppercase models: {remaining}")

    conn.close()
    print("Done.")


if __name__ == "__main__":
    uppercase_models()
