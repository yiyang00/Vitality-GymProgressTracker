from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import csv, sqlite3

app = Flask(__name__)

# registration interface 
@app.route('/', methods = ['GET', 'POST'])
def home():
  if request.method == 'POST':
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    if len(password) < 8: # validation for password
      error = "Password must be at least 8 characters long."
      return render_template('index.html', error=error)
    
    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", (username, password, email))
    conn.commit()
    conn.close()
  
  return render_template('index.html')

# login interface
@app.route('/login', methods = ['GET', 'POST'])
def login():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']

    conn = sqlite3.connect('accounts.db')
    c = conn.cursor()
    
    c.execute("SELECT * FROM users WHERE email=?", (email,))
    user = c.fetchone()

    if user: # if email exists
      stored_password = user[2]
      if password == stored_password: # successful login
        conn.close()
        return redirect(url_for('dashboard'))
      else: 
        error = "Incorrect email or password. Please try again." # mismatch
        conn.close()
        return render_template('login.html', error=error)
    else:
      error = "No user found with this email address." # details not found
      conn.close()
      return render_template('login.html', error=error)
  return render_template('login.html')

##@app.route('/dashboard', methods = ['GET', 'POST'])
##def dashboard():
##  if request.method == 'POST':
##    if request.form.get('c_exercise_name'):
##      c_exercise_name = request.form['c_exercise_name']
##      c_weight = request.form['c_weight']
##      c_repetitions = request.form['c_repetitions']
##      c_date = request.form['c_date']
##      return render_template('dashboard.html', c_exercise_name=c_exercise_name, c_weight=c_weight, c_repetitions=c_repetitions, c_date=c_date)
##    elif request.form.get('b_exercise_name'):
##      b_exercise_name = request.form['b_exercise_name']
##      b_weight = request.form['b_weight']
##      b_repetitions = request.form['b_repetitions']
##      b_date = request.form['b_date']
##      return render_template('dashboard.html', b_exercise_name=b_exercise_name, b_weight=b_weight, b_repetitions=b_repetitions, b_date=b_date)
##  return render_template('dashboard.html')

@app.route('/dashboard', methods = ['GET', 'POST'])
def dashboard():
  if request.method == 'POST':
    # input for chest
    if request.form.get('c_exercise_name'):
      conn = sqlite3.connect('tracker.db')
      c = conn.cursor()

      c_exercise_name = request.form['c_exercise_name']
      c_weight = request.form['c_weight']
      c_repetitions = request.form['c_repetitions']
      c_date = request.form['c_date']

      # Insert data into the 'chest' table
      c.execute("INSERT INTO chest (exercise_name, weight, repetitions, date) VALUES (?, ?, ?, ?)",
                (c_exercise_name, c_weight, c_repetitions, c_date))
      conn.commit()
      conn.close()

    # input for back
    elif request.form.get('b_exercise_name'):
      conn = sqlite3.connect('tracker.db')
      c = conn.cursor()

      b_exercise_name = request.form['b_exercise_name']
      b_weight = request.form['b_weight']
      b_repetitions = request.form['b_repetitions']
      b_date = request.form['b_date']

      # Insert data into the 'back' table
      c.execute("INSERT INTO back (exercise_name, weight, repetitions, date) VALUES (?, ?, ?, ?)",
                (b_exercise_name, b_weight, b_repetitions, b_date))
      conn.commit()
      conn.close()

    # input for arms
    elif request.form.get('ar_exercise_name'):
      conn = sqlite3.connect('tracker.db')
      c = conn.cursor()

      ar_exercise_name = request.form['ar_exercise_name']
      ar_weight = request.form['ar_weight']
      ar_repetitions = request.form['ar_repetitions']
      ar_date = request.form['ar_date']

      # Insert data into the 'arms' table
      c.execute("INSERT INTO arms (exercise_name, weight, repetitions, date) VALUES (?, ?, ?, ?)",
                (ar_exercise_name, ar_weight, ar_repetitions, ar_date))
      conn.commit()
      conn.close()

    # input for abdominals
    elif request.form.get('ab_exercise_name'):
      conn = sqlite3.connect('tracker.db')
      c = conn.cursor()

      ab_exercise_name = request.form['ab_exercise_name']
      ab_weight = request.form['ab_weight']
      ab_repetitions = request.form['ab_repetitions']
      ab_date = request.form['ab_date']

      # Insert data into the 'abdominals' table
      c.execute("INSERT INTO abdominals (exercise_name, weight, repetitions, date) VALUES (?, ?, ?, ?)",
                (ab_exercise_name, ab_weight, ab_repetitions, ab_date))
      conn.commit()
      conn.close()

    # input for legs
    elif request.form.get('l_exercise_name'):
      conn = sqlite3.connect('tracker.db')
      c = conn.cursor()

      l_exercise_name = request.form['l_exercise_name']
      l_weight = request.form['l_weight']
      l_repetitions = request.form['l_repetitions']
      l_date = request.form['l_date']

      # Insert data into the 'legs' table
      c.execute("INSERT INTO legs (exercise_name, weight, repetitions, date) VALUES (?, ?, ?, ?)",
                (l_exercise_name, l_weight, l_repetitions, l_date))
      conn.commit()
      conn.close()

    # input for shoulders
    elif request.form.get('s_exercise_name'):
      conn = sqlite3.connect('tracker.db')
      c = conn.cursor()

      s_exercise_name = request.form['s_exercise_name']
      s_weight = request.form['s_weight']
      s_repetitions = request.form['s_repetitions']
      s_date = request.form['s_date']

      # Insert data into the 'shoulders' table
      c.execute("INSERT INTO shoulders (exercise_name, weight, repetitions, date) VALUES (?, ?, ?, ?)",
                (s_exercise_name, s_weight, s_repetitions, s_date))
      conn.commit()
      conn.close()


##    conn = sqlite3.connect('tracker.db')
##    c = conn.cursor()
##    # Execute SQL query to find the max total volume achieved 
##    c.execute("""
##        SELECT MAX(total_product) AS max_total_product
##        FROM (
##            SELECT date, SUM(weight * repetitions) AS total_product
##            FROM chest
##            GROUP BY date
##        ) AS subquery
##    """)
##    max_volume = c.fetchone()[0]
##
##    conn.commit()
##    # Close the database connection
##    conn.close()
##
##    return render_template('dashboard.html', max_volume=max_volume)

##  return render_template('dashboard.html')

##@app.route('/get_volume')
##def calculate_volume():
  conn = sqlite3.connect('tracker.db')
  c = conn.cursor()
  # Execute SQL query to find the max total volume achieved

  # Volume to Maintain for Chest
  c.execute("""
      SELECT MAX(total_product) AS max_volume
      FROM (
          SELECT date, SUM(weight * repetitions) AS total_product
          FROM chest
          GROUP BY date
      ) AS subquery
""")
  c_max_volume = c.fetchone()[0]

  # Volume to Maintain for Back
  c.execute("""
    SELECT MAX(total_product) AS max_volume
    FROM (
        SELECT date, SUM(weight * repetitions) AS total_product
        FROM back
        GROUP BY date
    ) AS subquery
""")

  b_max_volume = c.fetchone()[0]

  # Volume to Maintain for Arms
  c.execute("""
    SELECT MAX(total_product) AS max_volume
    FROM (
        SELECT date, SUM(weight * repetitions) AS total_product
        FROM arms
        GROUP BY date
    ) AS subquery
""")

  ar_max_volume = c.fetchone()[0]

  # Volume to Maintain for Abdominals
  c.execute("""
    SELECT MAX(total_product) AS max_volume
    FROM (
        SELECT date, SUM(weight * repetitions) AS total_product
        FROM abdominals
        GROUP BY date
    ) AS subquery
""")

  ab_max_volume = c.fetchone()[0]

  # Volume to Maintain for Legs
  c.execute("""
    SELECT MAX(total_product) AS max_volume
    FROM (
        SELECT date, SUM(weight * repetitions) AS total_product
        FROM legs
        GROUP BY date
    ) AS subquery
""")

  l_max_volume = c.fetchone()[0]

  # Volume to Maintain for Shoulders
  c.execute("""
    SELECT MAX(total_product) AS max_volume
    FROM (
        SELECT date, SUM(weight * repetitions) AS total_product
        FROM shoulders
        GROUP BY date
    ) AS subquery
""")

  s_max_volume = c.fetchone()[0]
  
  conn.commit()
  conn.close() # close connection

  return render_template('dashboard.html', c_max_volume=c_max_volume, b_max_volume=b_max_volume, ar_max_volume=ar_max_volume, ab_max_volume=ab_max_volume, l_max_volume=l_max_volume, s_max_volume=s_max_volume)


@app.route('/history')
def history():
  conn = sqlite3.connect('tracker.db')
  c = conn.cursor()

  # select entries from 'chest' table
  c.execute("SELECT * FROM chest ORDER BY date DESC")
  c_rows = c.fetchall()

  # select entries from 'back' table
  c.execute("SELECT * FROM back ORDER BY date DESC")
  b_rows = c.fetchall()

  # select entries from 'arms' table
  c.execute("SELECT * FROM arms ORDER BY date DESC")
  ar_rows = c.fetchall()

  # select entries from 'abdominals' table
  c.execute("SELECT * FROM abdominals ORDER BY date DESC")
  ab_rows = c.fetchall()

  # select entries from 'legs' table
  c.execute("SELECT * FROM legs ORDER BY date DESC")
  l_rows = c.fetchall()

  # select entries from 'shoulders' table
  c.execute("SELECT * FROM shoulders ORDER BY date DESC")
  s_rows = c.fetchall()


  conn.commit()
  conn.close()

  return render_template('history.html', c_rows=c_rows, b_rows=b_rows, ar_rows=ar_rows, ab_rows=ab_rows, l_rows=l_rows, s_rows=s_rows)

  
if __name__ == '__main__':
  app.run(debug=True)
