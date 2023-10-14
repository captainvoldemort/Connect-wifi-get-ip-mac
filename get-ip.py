import socket

def get_ip_address():
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Use a sample remote server and port (can be any accessible server)
        s.connect(("8.8.8.8", 80))
        
        # Get the local IP address
        ip_address = s.getsockname()[0]
        
        return ip_address
    except Exception as e:
        print("Error:", str(e))

# Usage example
ip_address = get_ip_address()
if ip_address:
    print(f"Your Jetson device's IP address is: {ip_address}")
else:
    print("Failed to retrieve the IP address.")
