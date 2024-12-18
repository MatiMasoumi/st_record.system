from student_management_logic import atabaseConnection ,Application
if __name__ == "__main__":
    db_connection = DatabaseConnection()
    app = Application(db_connection)
    app.run()