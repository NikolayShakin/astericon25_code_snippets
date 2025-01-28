# Commands and code snippets used in the presentation on Astericon 2025
[Presentation. Asterisk as VoIP testing framework.](https://docs.google.com/presentation/d/e/2PACX-1vSKqdO_3McwfXZM5lCMDGwBlSO6aPtcdxQK-hi3iW89oz0eKwOa2eYjQp6SFHeVWQ/pub?start=false&loop=false&delayms=3000)
### Directory structure
```bash
.
├── README.md
├── ansible
│   ├── inventory
│   │   └── sip.yml
│   ├── playbooks
│   │   ├── configure_sip_service.yml
│   │   ├── configure_sip_tester.yml
│   │   └── install_asterisk.yml
│   ├── templates
│   │   ├── service_pjsip.conf.j2
│   │   ├── sip_users.yml
│   │   ├── tester_pjsip.conf.j2
│   │   └── tester_pjsip_nice.conf.j2
│   └── users.csv
├── asterisk
│   └── extensions.conf
└── call_generating_scripts
    ├── call.py
    └── call.sh
```

`asterisk/` - Asterisk dialplan examples

`ansible/` - Ansible playbooks used in the presentation

`call_generating_scripts/` - Bash/Python scripts for generating calls


Generate configuration for 'SIP service'
```bash
ansible-playbook playbooks/configure_sip_service.yml -i inventory/sip.yml
```

Generate basic configuration for sip-tester
```bash
ansible-playbook playbooks/configure_sip_tester.yml -i inventory/sip.yml -e nice=1
```

Generate advanced(randomized) configuration for sip-tester
```bash
ansible-playbook playbooks/configure_sip_tester.yml -i inventory/sip.yml
```

Basic call generation with asterisk CLI and originate command
```bash
asterisk -rx 'channel originate local/1234@testing application wait 10'
```

Generate up to 100 CPS(calls per second) with bash
```bash
while true; do asterisk -rx 'channel originate local/1234@testing application wait 10'; sleep 0.01; done
```

"Friendly scanning" extension range 1000-1300 with bash
```bash
for num in {1000..1300}; do asterisk -rx "channel originate local/$num@testing application wait 10"; sleep 0.01 ; done
```

Running prometheus  with docker
```bash
docker run \
    -p 9090:9090 \
    -v /root/prometheus.yml:/etc/prometheus/prometheus.yml \
    prom/prometheus
```

Running asterisk with local configuration but inside a docker container
```bash
docker run -d --rm  -v /etc/asterisk:/etc/asterisk  wazoplatform/asterisk:latest
```

