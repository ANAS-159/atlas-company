import ipaddress
import itertools
import sys
import yaml

with open('data/vlans.yml', encoding='utf-8') as f:
    vlans = yaml.safe_load(f)['vlans']
errors = []

ids = [v['id'] for v in vlans]
if len(ids) != len(set(ids)):
    errors.append('Duplicate VLAN identifier')
    
nets = [(v['name'], ipaddress.ip_network(v['ipv4']))
        for v in vlans if v.get('ipv4')]
for (n1, a), (n2, b) in itertools.combinations(nets, 2):
    if a.overlaps(b):
        errors.append(f'Overlap: {n1} {a} / {n2} {b}')
for e in errors:
    print(e)
print(f'{len(vlans)} VLANs read, {len(nets)} IPv4 networks checked, {len(errors)} error(s)')
sys.exit(1 if errors else 0)
