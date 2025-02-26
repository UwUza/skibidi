import socket
import json

UDP_IP = "127.0.0.1"  # Localhost
UDP_PORT = 9273  # Default port for RocketSimVis

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP socket

def send_state_to_rocketsimvis(game_state):
    """
    Send the game state to RocketSimVis via UDP
    :param game_state: The current state of the game to be visualized
    """
    # Convert the game state to JSON
    json_state = json.dumps(game_state)
    # Send the JSON data to RocketSimVis
    sock.sendto(json_state.encode('utf-8'), (UDP_IP, UDP_PORT))
