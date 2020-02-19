import psutil

vir_mem = psutil.virtual_memory()
used_mem = vir_mem.used
used_mem_per = int(vir_mem.percent)
used_cpu_per = int(psutil.cpu_percent())

print(psutil.net_connections())