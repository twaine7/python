import subprocess
"""

:rtype: dict or None
"""
cmd = "ping -n 1 {}".format("twitch.tv").split(' ')
output = subprocess.check_output(cmd).decode().strip()
lines = output.split("\n")
total = lines[-2].split(',')[3].split()[1]
loss = lines[-2].split(',')[2].split()[0]
timing = lines[-1].split()[3].split('/')
print( {
    'type': 'rtt',
    'min': timing[0],
    'avg': timing[1],
    'max': timing[2],
    'mdev': timing[3],
    'total': total,
    'loss': loss,
    })