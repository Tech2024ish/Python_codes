import sqlite3



def create_table(cursor):

    cursor.execute("DROP TABLE IF EXISTS Student ")

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS  Student(

        name TEXT,

        regno TEXT,

        school TEXT,

        dept TEXT,

        id_number INTEGER

    )""")

    cursor.execute("DROP TABLE IF EXISTS College")

    cursor.execute("""

        CREATE TABLE College(

        id INTEGER PRIMARY KEY,

        university TEXT, 

        academic_year TEXT)""")

    

def insert_records(cursor):

    records=[

        ("Claude","224010238","ICT","Computer-science",21),

        ("Muvara","224057809","Architecture","Visual-design",21), 

        ("Mubroke","224002631","Architecture","Visual-design",21),

        ("Jeannette","224009845","Education","Math-physics",21)

    ]

    cursor.executemany("INSERT INTO Student VALUES(?,?,?,?,?)",records)



    cursor.execute("""

    INSERT INTO College(id,university,academic_year) 

    VALUES(21,"University of Rwanda","Year1")""")



def fech_and_print(cursor):

    cursor.execute("""SELECT name,regno,school,dept,university,

    academic_year FROM Student JOIN College ON Student.id_number=College.id""")

    print("\n")

    print("Names:\t\tRegno:\t\tSchool:\t\t\tDepartment:\tUniversity:\tAcademic Year:\n")

    for record in cursor.fetchall():

        print(f"""{record[0]}\t\t{record[1]}\t{record[2]}\t\t{record[3]}\t{record[4]}\t{record[5]} \n""")



def main():

    try:



        connection=sqlite3.connect("Tech.db")

        cursor=connection.cursor()

        connection.commit()

        create_table(cursor)

        insert_records(cursor)

        fech_and_print(cursor)

        

    except sqlite3.Error as er:

        print(f"The database error {er} occured.")

    except Exception as e:

        print(f"Unecpected Error {e}.")

    finally:

        connection.close()



if __name__=="__main__":

    main()

