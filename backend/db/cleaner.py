import sys

from tables import Invoice, Claim, Employee, Admin
from setup import session, engine
from sqlalchemy import text


def confirm_deletion():
    """Ask for user confirmation before deletion"""
    print("⚠️  WARNING: This will delete ALL data from the following tables:")
    print("   - Claims")
    print("   - Invoices")
    print("   - Employees")
    print("   - Admins")
    print()

    response = input("Are you sure you want to continue? Type 'YES' to confirm: ")
    return response.upper() == "YES"


def get_table_counts(session):
    """Get current record counts for all tables"""
    counts = {}

    try:
        counts["claims"] = session.query(Claim).count()
        counts["invoices"] = session.query(Invoice).count()
        counts["employees"] = session.query(Employee).count()
        counts["admins"] = session.query(Admin).count()
    except Exception as e:
        print(f"Error getting table counts: {e}")
        counts = {"claims": 0, "invoices": 0, "employees": 0, "admins": 0}

    return counts


def delete_all_data():
    """Delete all data from tables in the correct order"""
    # Create database engine and session

    try:
        print("Connecting to database...")

        # Get initial counts
        print("Getting current record counts...")
        initial_counts = get_table_counts(session)

        print("\nCurrent record counts:")
        for table, count in initial_counts.items():
            print(f"  {table.capitalize()}: {count:,} records")

        total_records = sum(initial_counts.values())
        if total_records == 0:
            print("\nNo records found. Database is already empty.")
            return

        print(f"\nTotal records to delete: {total_records:,}")

        if not confirm_deletion():
            print("Deletion cancelled.")
            return

        print("\nStarting deletion process...")

        # Delete in correct order (child tables first due to foreign keys)
        deletion_order = [
            (Claim, "claims"),
            (Invoice, "invoices"),
            (Employee, "employees"),
            (Admin, "admins"),
        ]

        deleted_counts = {}

        for model_class, table_name in deletion_order:
            try:
                print(f"Deleting {table_name}...")

                # Get count before deletion
                count_before = session.query(model_class).count()

                if count_before > 0:
                    # Delete all records
                    deleted = session.query(model_class).delete()
                    session.commit()

                    deleted_counts[table_name] = deleted
                    print(f"  ✅ Deleted {deleted:,} records from {table_name}")
                else:
                    deleted_counts[table_name] = 0
                    print(f"  ℹ️  No records found in {table_name}")

            except Exception as e:
                session.rollback()
                print(f"  ❌ Error deleting from {table_name}: {e}")
                deleted_counts[table_name] = 0

        # Verify deletion
        print("\nVerifying deletion...")
        final_counts = get_table_counts(session)

        print("\nDeletion Summary:")
        print("-" * 50)
        for table_name in ["claims", "invoices", "employees", "admins"]:
            initial = initial_counts.get(table_name, 0)
            deleted = deleted_counts.get(table_name, 0)
            remaining = final_counts.get(table_name, 0)

            print(f"{table_name.capitalize()}:")
            print(f"  Initial: {initial:,}")
            print(f"  Deleted: {deleted:,}")
            print(f"  Remaining: {remaining:,}")

            if remaining == 0 and initial > 0:
                print("  Status: ✅ Successfully cleared")
            elif remaining == 0 and initial == 0:
                print("  Status: ℹ️  Was already empty")
            else:
                print(f"  Status: ⚠️  {remaining} records still remain")
            print()

        total_deleted = sum(deleted_counts.values())
        total_remaining = sum(final_counts.values())

        print(f"Total deleted: {total_deleted:,}")
        print(f"Total remaining: {total_remaining:,}")

        if total_remaining == 0:
            print("\n🎉 All data successfully deleted!")
        else:
            print(f"\n⚠️  Warning: {total_remaining} records still remain in database")

    except Exception as e:
        session.rollback()
        print(f"❌ Error during deletion process: {e}")

    finally:
        session.close()


def delete_specific_table(table_name):
    """Delete data from a specific table only"""
    table_map = {
        "claims": Claim,
        "invoices": Invoice,
        "employees": Employee,
        "admins": Admin,
    }

    if table_name.lower() not in table_map:
        print(f"❌ Invalid table name: {table_name}")
        print(f"Available tables: {', '.join(table_map.keys())}")
        return

    model_class = table_map[table_name.lower()]

    try:
        count_before = session.query(model_class).count()

        if count_before == 0:
            print(f"ℹ️  Table '{table_name}' is already empty.")
            return

        print(f"Found {count_before:,} records in '{table_name}' table.")

        response = input(
            f"Delete all {count_before:,} records from '{table_name}'? Type 'YES' to confirm: "
        )
        if response.upper() != "YES":
            print("Deletion cancelled.")
            return

        deleted = session.query(model_class).delete()
        session.commit()

        print(f"✅ Successfully deleted {deleted:,} records from '{table_name}' table.")

    except Exception as e:
        session.rollback()
        print(f"❌ Error deleting from '{table_name}': {e}")

    finally:
        session.close()


def drop_all_tables_cascade():
    """
    Drop all tables with CASCADE to handle foreign key constraints.
    """
    with engine.connect() as connection:
        result = connection.execute(
            text("""
            SELECT tablename 
            FROM pg_tables 
            WHERE schemaname = 'public'
        """)
        )

        tables = [row[0] for row in result]

        for table in tables:
            connection.execute(text(f'DROP TABLE IF EXISTS "{table}" CASCADE'))
            print(f"Dropped table: {table}")

        connection.commit()
        print("All tables dropped successfully with CASCADE.")


def show_help():
    """Show usage instructions"""
    print("Database Cleaner (Deletion) Utility")
    print("=" * 50)
    print("Usage:")
    print("  python cleaner.py --table claims     - Delete data from specific table")
    print("  python cleaner.py -t claims          - Shortcut for above")
    print("  python cleaner.py --drop-all-tables  - Drop (delete) all tables")
    print("  python cleaner.py --all              - Delete all data from every table")
    print("  python cleaner.py --help             - Show this help message")
    print("  python cleaner.py -h                 - Shortcut for above")
    print()
    print("Available tables: claims, invoices, employees, admins")
    print()
    print("⚠️  WARNING: This operation cannot be undone!")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--help" or sys.argv[1] == "-h":
            show_help()
        if sys.argv[1] == "--all":
            delete_all_data()
        if sys.argv[1] == "--drop-all-tables":
            drop_all_tables_cascade()
        elif (sys.argv[1] == "--table" or sys.argv[1] == "-t") and len(sys.argv) > 2:
            delete_specific_table(sys.argv[2])
        else:
            print("❌ Invalid arguments. Use --help for usage instructions.")
    else:
        print(
            "Need arguments to run database cleaner. Use --help for usage instructions."
        )
