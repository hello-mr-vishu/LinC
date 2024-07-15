import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    # Drop the job_portal_users table if it exists
    cur.execute("DROP TABLE IF EXISTS job_portal_users")
    
    with open('schema.sql', 'r') as f:
        conn.executescript(f.read())

    # Insert sample data
    cur.execute("INSERT INTO job_portal_users (name, email, phone, resume) VALUES (?, ?, ?, ?)",
                ('John Doe', 'john@example.com', '123-456-7890', 'resume_john_doe.pdf'))
    cur.execute("INSERT INTO job_portal_users (name, email, phone, resume) VALUES (?, ?, ?, ?)",
                ('Jane Smith', 'jane@example.com', '098-765-4321', 'resume_jane_smith.pdf'))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Database initialized with sample data.")
