import subprocess

def connect_to_wifi(ssid, password):
    try:
        cmd = "nmcli c down"
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        cmd = "nmcli dev wifi list"
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

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
wifi_ssid = "SSID_HERE"
wifi_password = "PASSWORD_HERE"
connect_to_wifi(wifi_ssid, wifi_password)
