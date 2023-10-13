import subprocess

def disconnect_from_wifi():
    try:
        # Disconnect from the current connection
        cmd = "nmcli c down"
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if result.returncode == 0:
            print("Disconnected from the previous network.")
        else:
            print("Failed to disconnect from the previous network.")
            print(result.stderr.decode('utf-8'))
    except Exception as e:
        print("Error:", str(e)

def connect_to_wifi(ssid, password):
    try:
        # Disconnect from the previous network
        disconnect_from_wifi()
        
        # Check if the Wi-Fi network is already in the list of known networks
        cmd = f"nmcli c s | grep '{ssid}'"
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode == 0:
            # If the network is already in the list, you can activate it
            cmd = f"nmcli c up '{ssid}'"
        else:
            # If the network is not in the list, add it and then activate
            cmd = f"nmcli d wifi connect '{ssid}' password '{password}'"

        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode == 0:
            print(f"Connected to {ssid} successfully.")
        else:
            print(f"Failed to connect to {ssid}.")
            print(result.stderr.decode('utf-8'))

    except Exception as e:
        print("Error:", str(e))

# Usage example
wifi_ssid = "YourWiFiNetwork"
wifi_password = "YourWiFiPassword"
connect_to_wifi(wifi_ssid, wifi_password)