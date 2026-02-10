from app import app, db

with app.app_context():
    print("Connecting to database...")

    # 1. Delete everything
    print("Deleting all existing tables...")
    db.drop_all()

    # 2. Recreate empty tables
    print("Creating new tables...")
    db.create_all()

    print("Success! Database has been reset.")
    print("Run 'python app.py' now to seed the default resume data.")