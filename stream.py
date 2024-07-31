import socketio
import json
import time
import threading
from dotenv import load_dotenv
import os

load_dotenv()

# Create a Socket.IO client
sio = socketio.Client()

# Define the JSON object to be sent
with open('data.json', 'r') as file:
    data = json.load(file)

# Define the server URL
SERVER_URL = os.getenv('SERVER_URL')

# Connect to the Socket.IO server
@sio.event
def connect():
    print('Connection established')
    # Start sending data after connection is established
    threading.Thread(target=send_data).start()
    threading.Thread(target=send_first).start()

@sio.event
def disconnect():
    print('Disconnected from server')

@sio.event
def connect_error(data):
    print('Connection failed:', data)

def send_first():
    try:
        for log in data['geometry']['coordinates'][1]:
            item = {
                "obligor": "Maidport1024",
                "message": {
                    "device": "9496e2f0-aaae-4a37-b899-0970c86add6a",
                    "lat": log[0],
                    "lon": log[1],
                    "speed": 40,
                    "sat":3
                }
            }
            sio.emit('message', item)
            time.sleep(2)
        print('Finished sending data')
    except Exception as e:
        print('Error sending data:', e)
    finally:
        # Optionally disconnect after sending all data
        sio.disconnect()

# Function to send data
def send_data():
    try:
        for log in data['geometry']['coordinates'][0]:
            item = {
                "obligor": "Maidport1024",
                "message": {
                    "device": "04adea1b-eab3-48c8-bd11-a285a0f967f9",
                    "lat": log[0],
                    "lon": log[1],
                    "speed": 40,
                    "sat":3
                }
            }
            sio.emit('message', item)
            time.sleep(1)
        print('Finished sending data')
    except Exception as e:
        print('Error sending data:', e)
    finally:
        # Optionally disconnect after sending all data
        sio.disconnect()

# Main function
def main():
    try:
        # Connect to the server
        sio.connect(SERVER_URL, headers={'token': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvYmxpZ29yIjoiTWFpZHBvcnQxMDI0IiwiZGV2aWNlSWQiOiIxMjM0NTYiLCJuYW1lIjoiRGV2aWNlIDEiLCJpYXQiOjE3MjI0MTAxNDl9._qtYj8tT-oHV16u8FC3zJQuMMItUTWONorHqQnXbb9I"})
        # Keep the script running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('Script interrupted by user')
    except Exception as e:
        print('Error:', e)
    finally:
        sio.disconnect()

if __name__ == "__main__":
    main()
