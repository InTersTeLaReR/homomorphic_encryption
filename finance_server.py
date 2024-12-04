from flask import Flask, request, jsonify, render_template
from phe import paillier

app = Flask(__name__)

# Load or generate keys securely
public_key, private_key = paillier.generate_paillier_keypair()

# In-memory storage (replace with a database in production)
financial_data = {}

@app.route('/')
def home():
    return render_template('finance_index.html', transactions=financial_data)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    user_id = data.get('user_id')
    encrypted_transaction = data.get('encrypted_transaction')
    
    # Decrypt the data
    encrypted_number = paillier.EncryptedNumber(public_key, int(encrypted_transaction['ciphertext']), int(encrypted_transaction['exponent']))
    decrypted_amount = private_key.decrypt(encrypted_number)
    
    # Store decrypted data
    financial_data[user_id] = decrypted_amount
    
    return jsonify({"message": "Transaction decrypted and stored successfully."})

if __name__ == '__main__':
    app.run(debug=True)
