# Cisco Network Automation Script  

This Python script automates the configuration of OSPF (Open Shortest Path First) on Cisco network devices. It uses the `Netmiko` library to establish SSH connections and configure devices securely.

## Features  

- Connect to multiple Cisco devices via SSH  
- Validate IP addresses before configuration  
- Ensure no duplicate device configuration  
- Configure OSPF process ID and networks dynamically  
- Handle authentication and timeout errors gracefully  

---

## Prerequisites  

Ensure you have the following installed before running the script:  

- Python 3.6 or higher  
- Required Python modules:  
  ```bash
  pip install netmiko


Sample Output:

*************************************************
How many devices would you like to configure? 1  
Enter device IP: 192.168.1.1  
Enter Username: admin  
Enter Password: ********  
Enter Secret: ********  
Connecting to host 192.168.1.1....  
Enter the process ID: 1  
How many networks would you like to configure? 2  
Enter the network: 192.168.10.0  
Enter the wild card mask: 0.0.0.255  
Enter the area number: 0  
Device "Router1" has been configured!  
*************************************************


Error Handling

    Invalid IP Address: The script checks for valid IPv4 addresses.
    Duplicate Device: Ensures no duplicate configurations for the same device IP.
    Authentication Errors: If login credentials are incorrect, an error message is displayed.
    Timeout Errors: If the device is unreachable, a timeout error message is shown.
