from netmiko import ConnectHandler, NetMikoAuthenticationException, NetMikoTimeoutException
from getpass import getpass
import ipaddress

no_of_devices = int(input('How many devices would you like to configure? '))
ip_add_list = []

for device in range (no_of_devices):
    while True:
        ip_add = input('Enter device IP: ')
        
        try:
            ipaddress.IPv4Address(ip_add)
        except ipaddress.AddressValueError:
            print('Error: Invalid IP address! Try again.')
            continue
        
        if ip_add in ip_add_list:
            print('Error: This device has been already configured! Try another one.')
            continue
        else:
            ip_add_list.append(ip_add)
            break

    username = input('Enter Username: ')
    password = getpass('Enter Password: ')
    secret = getpass('Enter Secret: ')

    device = {
            'device_type' : 'cisco_ios',
            'host' : ip_add,
            'username' : username,
            'password' : password,
            'secret' : secret
    }
   
    try:
        net_connect = ConnectHandler(**device)
        net_connect.enable()

        print(f'Connecting to host {ip_add}....')
        show_name = net_connect.send_command('show run | inc hostname').split()
        device_name = show_name[1]

        process_ID = int(input('Enter the process ID: '))
        no_of_networks = int(input('How many networks would you like to configure? '))

        for network in range (no_of_networks):
            network = input('Enter the network: ')
            wildcard = input('Enter the wild card mask: ')
            ospf_area = input('Enter the area number: ')
            
            commands = [f'router ospf {process_ID}', f'network {network} {wildcard} area {ospf_area}']
            output = net_connect.send_config_set(commands)

            print(output)
            print(f'Device "{device_name}" has been configured!')
    except NetMikoAuthenticationException:
        print(f'Error: Authentication Failed for host {ip_add}! Please check the credentials.')
    except NetMikoTimeoutException:
        print(f'Error: Timeout while connecting to host {ip_add}! This device might be unreachable.')

