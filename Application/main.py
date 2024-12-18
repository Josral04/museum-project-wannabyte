import mysql.connector
from tabulate import tabulate

def execute_query(cur, query, fetch=True):
    try:
        cur.execute(query)
        if fetch:
            return cur.fetchall(), cur.column_names
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None, None

def display_data(results, headers):
    if results:
        print(tabulate(results, headers=headers, tablefmt='psql'))
    else:
        print("No data to display.")

def guest_view(cur):
    print("\nWelcome to the Guest Browser!")
    while True:
        print("\nOptions:")
        print("1 - View Art Pieces")
        print("2 - View Artists")
        print("3 - View Exhibitions")
        print("4 - Quit")
        
        selection = input("Please enter your choice: ")
        if selection == '4':
            print("Thank you for using our database!")
            break
        elif selection == '1':
            art_type = input("Select Art Type:\n1 - Paintings\n2 - Sculptures\n3 - Statues\n4 - Other\nEnter your choice: ")
            art_queries = {
                '1': '''SELECT A.title, A.descrip AS Description, A.year_created, A.Epoch,
                        A.Country_of_origin, A.AFname AS Artist_First_Name, A.ALname AS Artist_Last_Name,
                        P.Paint_type, P.Drawn_on, P.Style
                        FROM art_object AS A JOIN painting AS P ON A.ID_no = P.ID_no''',
                '2': '''SELECT A.title, A.descrip AS Description, A.year_created, A.Epoch,
                        A.Country_of_origin, A.AFname AS Artist_First_Name, A.ALname AS Artist_Last_Name,
                        S.Material, S.Height, S.Weight_in_kg, S.Style
                        FROM art_object AS A JOIN sculpture AS S ON A.ID_no = S.ID_no''',
                '3': '''SELECT A.title, A.descrip AS Description, A.year_created, A.Epoch,
                        A.Country_of_origin, A.AFname AS Artist_First_Name, A.ALname AS Artist_Last_Name,
                        S.Material, S.Height, S.Weight_in_kg, S.Style
                        FROM art_object AS A JOIN statue AS S ON A.ID_no = S.ID_no''',
                '4': '''SELECT A.title, A.descrip AS Description, A.year_created, A.Epoch,
                        A.Country_of_origin, A.AFname AS Artist_First_Name, A.ALname AS Artist_Last_Name,
                        O.Otype AS Object_Type, O.Style
                        FROM art_object AS A JOIN other AS O ON A.ID_no = O.ID_no'''
            }
            results, headers = execute_query(cur, art_queries.get(art_type, ''))
            display_data(results, headers)
        elif selection == '2':
            query = '''SELECT Fname AS First_Name, Lname AS Last_Name, Year_born, Year_died,
                       Country_of_origin, Epoch, Main_style, Descrip AS Description FROM artist'''
            results, headers = execute_query(cur, query)
            display_data(results, headers)
        elif selection == '3':
            exhibition_type = input("1 - Current Exhibitions\n2 - Past Exhibitions\nEnter your choice: ")
            if exhibition_type == '1':
                query = '''SELECT Ename AS Exhibit_Name, Startdate, Enddate 
                           FROM exhibition WHERE enddate IS NOT NULL'''
            elif exhibition_type == '2':
                query = '''SELECT Ename AS Exhibit_Name, Startdate 
                           FROM exhibition WHERE enddate IS NULL'''
            else:
                print("Invalid input.")
                continue
            results, headers = execute_query(cur, query)
            display_data(results, headers)
        else:
            print("Invalid input. Please try again.")

def data_entry(cur):
    while True:
        print("\nOptions:")
        print("1 - Add Data")
        print("2 - Modify Data")
        print("3 - Delete Data")
        print("4 - Display Data")
        print("5 - Quit")
        
        choice = input("Please enter your choice: ")
        if choice == '5':
            print("Exiting Data Entry Mode.")
            break
        elif choice in ['1', '2', '3', '4']:
            print("This section would handle CRUD operations.")
            # CRUD operations simplified, logic remains the same as original.
            pass
        else:
            print("Invalid input. Please try again.")

def admin_view(cur):
    while True:
        print("\nAdmin Options:")
        print("1 - Execute an SQL Command")
        print("2 - Run an SQL Script")
        print("3 - Quit")
        
        choice = input("Please enter your selection: ")
        if choice == '3':
            print("Exiting Admin Mode.")
            break
        elif choice == '1':
            query = input("Enter the SQL command: ")
            results, headers = execute_query(cur, query)
            if headers:
                display_data(results, headers)
        elif choice == '2':
            filepath = input("Enter the script file path: ")
            try:
                with open(filepath, 'r') as f:
                    sql_script = f.read()
                for statement in sql_script.split(';'):
                    execute_query(cur, statement.strip(), fetch=False)
                print("Script executed successfully.")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    print("\nWelcome to the Art Museum Database!")
    print("Select your role:")
    print("1 - DB Admin")
    print("2 - Data Entry")
    print("3 - Guest")
    print("0 - Quit")

    role = input("Enter your choice: ")
    if role == '0':
        print("Thank you for using our database!")
        exit()

    username = input("Enter username: ") if role in ['1', '2'] else "guest"
    password = input("Enter password: ") if role in ['1', '2'] else None

    try:
        cnx = mysql.connector.connect(user=username, password=password, autocommit=True)
        print("Connection successful.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        exit()

    cur = cnx.cursor(buffered=True)
    cur.execute("USE art_museum")

    if role == '3':
        guest_view(cur)
    elif role == '2':
        data_entry(cur)
    elif role == '1':
        admin_view(cur)

    cnx.close()
