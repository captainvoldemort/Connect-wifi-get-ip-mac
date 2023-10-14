# **Python Scripts for Jetson Device Configuration**

This repository contains three Python scripts to help configure your Jetson device's Wi-Fi connection and retrieve the IP and MAC addresses.

## **`connect-wifi.py`**

This script allows you to connect to a specific Wi-Fi network by providing the SSID and password. It performs the following tasks:

1. Disconnects from the current network, if connected.
2. Lists available Wi-Fi networks.
3. Checks if the desired network (SSID) is already in the list of known networks.
4. If the network is found, it activates the connection.
5. If the network is not found, it adds the network and activates the connection.

### **Usage**

Replace **`"SSID_HERE"`** and **`"PASSWORD_HERE"`** in the script with your Wi-Fi network's SSID and password. Run the script with Python to connect to the desired Wi-Fi network.

Example:

```bash
python connect-wifi.py

```

## **`get-ip.py`**

This script retrieves the IP address of your Jetson device by creating a socket connection to a sample remote server. It performs the following task:

1. Creates a socket object.
2. Connects to a remote server (8.8.8.8) and port (80).
3. Gets the local IP address of the device.

### **Usage**

Run the script with Python to retrieve the IP address of your Jetson device.

Example:

```bash
python get-ip.py

```

## **`get-mac.py`**

This script retrieves the MAC (Media Access Control) address of your Jetson device. It utilizes the **`psutil`** and **`uuid`** modules to obtain the MAC address of the default network interface.

### **Usage**

Run the script with Python to retrieve the MAC address of your Jetson device.

Example:
```bash
python get-mac.py

```
