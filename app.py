from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-command', methods=['POST'])
def send_command():
    command_data = request.get_json()
    print('Received command from the web page:', command_data)
    
    # Simulate Arduino behavior (modify this part based on your Arduino code)
    if 'command' in command_data:
        if command_data['command'] == 'LED_ON':
            # Simulate turning on an LED (adjust pin number as needed)
            print('Simulating LED_ON command')
        elif command_data['command'] == 'LED_OFF':
            # Simulate turning off an LED (adjust pin number as needed)
            print('Simulating LED_OFF command')

    response_data = {'message': 'Command processed successfully'}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
