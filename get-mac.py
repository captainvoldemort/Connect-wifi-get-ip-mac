import psutil

def get_mac_address():
    try:
        # Get the MAC address of the default network interface
        mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in (0, 8, 16, 24, 32, 40)])
        return mac_address
    except Exception as e:
        print("Error:", str(e))

# Usage example
mac_address = get_mac_address()
if mac_address:
    print(f"Your Jetson device's MAC address is: {mac_address}")
else:
    print("Failed to retrieve the MAC address.")
