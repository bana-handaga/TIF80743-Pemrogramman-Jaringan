import ipaddress as ip

CLASS_C_ADDR = '192.168.0.0'  #ip network
# alternatif 172.16.x.x atau 10.x.x.x

if __name__ == '__main__'  :
	not_configed = True
	while not_configed:
		IPADDRESS = input("IP ADDRESS: (172.16.10.1): ")
		# prefix = input("Masukan prefix (24-30): ")
		prefix = input("Masukan prefix (8-30): ")		
		prefix = int(prefix) #pastikan berupa angka
		# if prefix not in range(23,31):
		if prefix not in range(7,31):
			# raise Exception("Prefix harus diantara 24-30")
			raise Exception("Prefix harus diantara 8-30")
		# net_addr = CLASS_C_ADDR + '/' + str(prefix)
		net_addr = IPADDRESS + '/' + str(prefix)
		IP4 = ip.IPv4Interface(net_addr)
		print("IP Address: %s " %net_addr)
		try:
			# mengidentifikasi IP NETWORK
			network = ip.ip_network(str(IP4.network)) 
		except:
			raise Exception("Ada kesalahan Network address ")
		print("Jumlah IP Address: %s" %(network.num_addresses))
		print("IP Network:        %s" %str(network.network_address))
		print("Sub netmask:       %s" %str(network.netmask))
		print("IP Broadcast:      %s" %str(network.broadcast_address))
		IP_PERTAMA = list(network.hosts())[0]
		IP_TERAKHIR = list(network.hosts())[-1] #index terakhir
		JUMLAH_IP_HOST = len(list(network.hosts())) #network.num_addresses - 2
		print("IP host pertama:   %s" %(IP_PERTAMA))
		print("IP host terakhir:  %s" %(IP_TERAKHIR))
		print("Jumlah IP host:  %s" %(JUMLAH_IP_HOST))


		ok = input("Apakah sudah betul [y/n]? ")
		ok = ok.lower() #merubah menjadi huruf kecil
		if ok.strip() == 'y':
			not_configed = False
    




