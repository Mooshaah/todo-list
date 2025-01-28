from sqlalchemy.orm import Session
from models.database import SessionLocal

import database,task
# Create dummy data
def seed_data():
    db: Session = SessionLocal()
    try:
        # Add dummy tasks
        task1 = task.Task(id = 1, title= "first task", description= "first task on the todo list", due_date="1/30/25", completed=False)
        task2 = task.Task(id = 2, title= "Second Task", description= "Second task on the todo list", due_date="1/30/25", completed=True)
        db.add(task1)
        db.add(task2)

        db.commit()  # Save changes to the database
        print("Dummy data added successfully!")
    except Exception as e:
        print(e)
        db.rollback()
    finally:
        db.close()

# Run the seeding function
if __name__ == "__main__":
    seed_data()
