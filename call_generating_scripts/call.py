import socket

ami_login = """Action: Login
Username: tester
Secret: 1234

"""
ami_originate = """Action: Originate
Channel: pjsip/dummy_endpoint/sip:111222333@216.128.176.244
Application: Playback
Data: beep
CallerID: "Bob" <987654321>
Timeout: 30000

"""
ami_logoff = "Action: Logoff\n\n"

def send_ami_command(command,socket=None):
        socket.sendall(command.encode())
        response = socket.recv(4096)
        print(response.decode())

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 5038))
        send_ami_command(ami_login,s)
        send_ami_command(ami_originate,s)
        send_ami_command(ami_logoff,s)