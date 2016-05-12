with open('test.bat', 'w') as inf:
    for i in range(2, 16):
        if i not in [11, 12, 14]:
            inf.write('python run_car.py -s 1000 --seed {} -f network_config_agent_0_layers_9_18_9_1.txt -e True\n'.format(i))

with open('train.bat', 'w') as inf:
    inf.write('python run_car.py -s 1000 --seed 3 -f weights_step2.txt\n')
    for i in [5, 13, 15]:
        inf.write('python run_car.py -s 1000 --seed {} -f network_config_agent_0_layers_9_18_9_1.txt\n'.format(i))