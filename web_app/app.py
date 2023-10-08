from flask import Flask, render_template, jsonify, request
import csv
import json

app = Flask(__name__)

# Function to load the config.json file
def load_config():
    with open('../config.json', 'r') as config_file:
        config_data = json.load(config_file)
    return config_data

@app.route('/')
def index():
    # Load the config data
    config_data = load_config()

     # Access the CLIENT_NAME value
    client_name = config_data.get('CLIENT_NAME', 'Default Client Name')

    return render_template('index.html',client_name=client_name)

#get 10 last rows of data
@app.route('/get_data')
def get_data():
    data = []

    # Read the CSV file containing your data
    with open('../data/public_network_data.csv', mode='r', encoding='utf-8-sig', newline='') as file:
        reader = csv.DictReader(file)

        for index, row in enumerate(reader, start=1):
            classes = ['FALSE POSITIVE', 'CONFIRMED', 'CANDIDATE']
            data.append({
                'id': index,  
                'source': row['source'],
                'koi_disposition': classes[int(row['koi_disposition'])],
                'probability': row['probability'],
            })

    # Slice the data to show only the last 10 rows
    last_10_data = data[-10:]

    # Return the last 10 rows of data as JSON to the client
    return jsonify(last_10_data)

# Get the specific data with the row_id
@app.route('/get_data_from_id/<int:row_id>')
def get_data_from_id(row_id):
    data = []

    # Initialize a counter for generating unique IDs
    unique_id_counter = 1

    # Read the CSV file containing your data
    with open('../data/public_network_data.csv', mode='r', encoding='utf-8-sig', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            classes = ['FALSE POSITIVE', 'CONFIRMED', 'CANDIDATE']
            row_data = {
                'id': unique_id_counter,  
                'source': row['source'],
                'koi_score': row['koi_score'],
                'koi_fpflag_nt': row['koi_fpflag_nt'],
                'koi_fpflag_ss': row['koi_fpflag_ss'],
                'koi_fpflag_co': row['koi_fpflag_co'],
                'koi_impact': row['koi_impact'],
                'koi_model_snr': row['koi_model_snr'],
                'koi_steff': row['koi_steff'],
                'koi_slogg': row['koi_slogg'],
                'ra': row['ra'],
                'dec': row['dec'],
                'koi_disposition': classes[int(row['koi_disposition'])],
                'probability': row['probability'],
            }

            # Increment the unique ID counter
            unique_id_counter += 1

            # If 'id' parameter is provided, check if the generated 'id' matches the specified 'row_id'
            if row_data['id'] == row_id:
                data.append(row_data)
                break  # Stop searching after finding the matching row

    # Return the data as JSON to the client
    return jsonify(data) 


@app.route('/get_dynamic_data_info')
def get_dynamic_data_info():
    # Load the config data
    config_data = load_config()

     # Access the CLIENT_NAME value
    client_name = config_data.get('CLIENT_NAME', 'Default Client Name')
    return render_template('dynamic_data_info.html',client_name=client_name)

if __name__ == '__main__':
    app.run(debug=True)

# show whole file -----------------------------------------------------------------
# @app.route('/get_all_data')
# def get_data():
#     data = []

#     # Read the CSV file containing your data
#     with open('../data/public_network_data.csv', mode='r', newline='') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             data.append(row)

#     # Return the data as JSON to the client
#     return jsonify(data)
# ----------------------------------------------------------------------------------------------------------------------------------
# Hambam version
# @app.route('/get_data')
# def get_data():
#     data = []

#     # Read the CSV file containing your data
#     with open('./data/public_network_data.csv', mode='r',encoding='utf-8-sig', newline='') as file:
#         reader = csv.DictReader(file)
#         all_rows =[]
#         # select only columns of interest
#         for row in reader:
#             classes = ['FALSE POSITIVE', 'CONFIRMED', 'CANDIDATE']
#             data.append({
#                 'source': row['source'],
#                 'koi_disposition': classes[int(row['koi_disposition'])],
#                 'probability': row['probability'],
#             })
        
#         # Determine the starting index for the last 10 rows
#         start_index = max(0, len(all_rows) - 10)
        
#         # Select the last 10 rows
#         last_10_rows = all_rows[start_index:]

#     # Return the data as JSON to the client
#     return jsonify(data)
