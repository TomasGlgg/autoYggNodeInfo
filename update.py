import json, subprocess


def update_config(data):  # update config
    settings = json.load(open('settings.json'))
    for name in settings:
        command = settings[name]
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        command_out = process.communicate()[0].decode().strip()
        data['NodeInfo'][name] = command_out


def delete_comments(data):
    data = data.split('\n')
    out_data = ''
    for line in data:
        line = line.strip()
        if line.count('#') > 0:
            if line[0] == '#':
                out_data += '\n'
            else:
                out_data += line[:line.index('#')] + '\n'
        else:
            out_data += line
    return out_data


def save_config(data, output_config):
    file = open(output_config, 'w')
    json.dump(data, file, sort_keys=True, indent=4)
    file.close()


if __name__ == '__main__':
    from sys import argv
    input_config = argv[1]
    output_config = argv[2]

    #  $ python3 update.py /etc/yggdrasil.conf /etc/yggdrasil.conf

    print('Opening input config...')
    raw = open(input_config).read()
    print('Input config loaded, updating config...')
    raw = delete_comments(raw)
    data = json.loads(raw)
    update_config(data)
    print('Config updated, saving...')
    save_config(data, output_config)
    print('Config saved, reloading yggdrasil...')
    subprocess.Popen(['sudo', 'systemctl', 'reload', 'yggdrasil'])
    print('Done.')
