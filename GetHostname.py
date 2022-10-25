import socket
import csv
import sys




ping_results = []

def ping_request(server_ip):
 ping_answer=socket.gethostbyaddr(server_ip)
 return ping_answer

with open(sys.argv[1], mode='r') as host_ip:
		host_ip = csv.DictReader(host_ip, delimiter=",", fieldnames=['ip'])
		for row in host_ip:
			server_ip = row['ip']
			print(server_ip)
			try:
				ping_results.append([server_ip,ping_request(server_ip)])
			except Exception as e:
				ping_results.append([server_ip,e])


with open("results.csv", mode='w') as csv_file:
    csv_writer = csv.writer(csv_file,delimiter=",")
    csv_writer.writerows(ping_results)
