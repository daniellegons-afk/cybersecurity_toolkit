import socket

def run_scanner():
    target = input("please enter a target: ")
    start_port = int(input("please enter a start port: "))
    end_port = int(input("please enter a end port: "))
    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} is open")
            open_ports.append(port)
        else:
            print(f"The port {port} is closed")
        sock.close()

    with open("scan_results.txt",  "w") as file:
       for port in open_ports:     
            file.write(f"{port}\n") 

    with open ("scan_results.txt","r") as file:
        content = file.read()
        print(content)  