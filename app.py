from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.security import generate_password_hash
import pymysql

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database connection function
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',  # replace with your MySQL username
        password='143543',  # replace with your MySQL password
        database='spotify_clone'  # replace with your database name
    )

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            # Get form data
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            
            # Hash the password before saving it
            hashed_password = generate_password_hash(password)
            
            # Check if the username already exists
            connection = get_db_connection()
            with connection.cursor() as cursor:
                # Check if username exists
                cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
                existing_user = cursor.fetchone()

                if existing_user:
                    return jsonify({'error': 'Username already taken!'}), 400

                # Insert the new user into the database with the hashed password and email
                cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", 
                               (username, email, hashed_password))
                connection.commit()  # Commit the transaction

            connection.close()  # Close the connection after the operation is done
            return redirect(url_for('login'))  # Redirect to login after registration
        
        except pymysql.MySQLError as e:
            # Catch MySQL errors
            print(f"MySQL error: {e}")
            return jsonify({'error': 'Database error occurred!'}), 500
        except Exception as e:
            # Catch any other errors
            print(f"Unexpected error: {e}")
            return jsonify({'error': 'An unexpected error occurred!'}), 500

    return render_template('register.html')

# Login route
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()  # Get JSON data from the request body
        username = data['username']
        password = data['password']
        
        # Logic to authenticate the user goes here...
        
        return jsonify({'message': 'Login successful!'})
    except Exception as e:
        # Handle any errors that might occur during login
        print(f"Error in login: {e}")
        return jsonify({'error': 'An error occurred during login!'}), 500

if __name__ == "__main__":
    app.run(debug=True)
