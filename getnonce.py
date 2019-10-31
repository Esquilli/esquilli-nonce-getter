import subprocess, time

# Command: ideviceinfo
print("[*] Command: ideviceinfo")
info = str(subprocess.check_output(["ideviceinfo"]))

# Get required info
ecid = [s for s in info.split("\\r\\n") if "UniqueChipID" in s][0].split(" ")[1]
udid = [s for s in info.split("\\r\\n") if "UniqueDeviceID" in s][0].split(" ")[1]
production_type = [s for s in info.split("\\r\\n") if "ProductType" in s][0].split(" ")[1]

# Command: ideviceenterrecovery UDID
print("[*] Command: ideviceenterrecovery %s" % udid)
subprocess.check_output(["ideviceenterrecovery", udid])
time.sleep(20)

while True:
	try:
		# Command: irecovery -q and get NONC
		nonc = str(subprocess.check_output(["irecovery", "-q"])).split("\\r\\n")[-4].split(" ")[1]
		print("[*] Command: irecovery -q")
		break
	except Exception as e:
		print("[!] Waiting for device to reconnect.")
		continue

# Command: irecovery -n and finish process
print("[*] Command: irecovery -q")
subprocess.check_output(["irecovery", "-n"])
print("[*] Your ECID is %s" % ecid)
print("[*] Your NONC is %s" % nonc)
print("[*] Your Production Type is %s" % production_type)

# Output to file
with open('nonce.txt', 'w') as file:
	file.write("ECID: " + ecid + "\n")
	file.write("NONC: " + nonc + "\n")
	file.write("Production Type: " + production_type + "\n")
	print("[*] Output saved to nonce.txt file")

# Done
print("[!] Follow me on Twitter @EsquilliDev")
input("Press Enter to exit...")
