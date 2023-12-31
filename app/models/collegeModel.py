from app import mysql

class CollegeModel:
    # Get ALL COLLEGES  
    @classmethod
    def get_colleges(cls):
        try:
            cur = mysql.connection.cursor()
            sql = '''SELECT * FROM college'''
            cur.execute(sql)
            college = cur.fetchall()
            return college
        except Exception as e:
            return f"Failed to load College List: {str(e)}"
        
    @classmethod
    def add_college(cls, code, name):
        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO `college` (`college_code`, `college_name`) VALUES (%s, %s)",
                (code, name),
            )
            mysql.connection.commit()
            return "Faculty created successfully!"
        except Exception as e:
            return f"Failed to create College: {str(e)}"