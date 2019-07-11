import ipaddress


class ObscureIP(ipaddress.IPv4Address):
    def __init__(self, address, auto_obscure=True):
        super().__init__(address)
        if auto_obscure:
            self.obscure()

    def obscure(self):
        _bytes = int.to_bytes(self._ip, 4, 'big')
        first_two = int.from_bytes(_bytes[0:2], 'big')
        first_three = int.from_bytes(_bytes[0:3], 'big')
        all_int = int.from_bytes(_bytes[0:4], 'big')
        middle_two = int.from_bytes(_bytes[1:3], 'big')
        last_two = int.from_bytes(_bytes[-2:], 'big')
        last_three = int.from_bytes(_bytes[-3:], 'big')
        print(all_int)       
        print(str(self))
        print(f'{_bytes[0]}.{_bytes[1]}.{last_two}')
        print(f'{_bytes[0]}.{last_three}')
        print(hex(all_int))
        print(f'{hex(_bytes[0])}.{hex(_bytes[1])}.{hex(_bytes[2])}.{hex(_bytes[3])}')
        print(f'{hex(_bytes[0])}.{_bytes[1]}.{hex(_bytes[2])}.{hex(_bytes[3])}')
        print(f'{hex(_bytes[0])}.{hex(_bytes[1])}.{_bytes[2]}.{hex(_bytes[3])}')
        print(f'{hex(_bytes[0])}.{hex(_bytes[1])}.{hex(_bytes[2])}.{_bytes[3]}')
        print(f'{_bytes[0]}.{_bytes[1]}.{hex(last_two)}')
        print(f'{_bytes[0]}.{hex(_bytes[1])}.{hex(last_two)}')
        print(f'{_bytes[0]}.{hex(last_three)}')
        print(f'0{oct(all_int)}'.replace('0o', ''))
        print(f'0{oct(_bytes[0])}.0{oct(_bytes[1])}.0{oct(_bytes[2])}.0{oct(_bytes[3])}'.replace('0o', ''))
        print(f'0{oct(_bytes[0])}.{_bytes[1]}.0{oct(_bytes[2])}.0{oct(_bytes[3])}'.replace('0o', ''))
        print(f'0{oct(_bytes[0])}.0{oct(_bytes[1])}.{_bytes[2]}.0{oct(_bytes[3])}'.replace('0o', ''))
        print(f'0{oct(_bytes[0])}.0{oct(_bytes[1])}.0{oct(_bytes[2])}.{_bytes[3]}'.replace('0o', ''))
        print(f'{_bytes[0]}.{_bytes[1]}.0{oct(last_two)}'.replace('0o', ''))
        print(f'{_bytes[0]}.0{oct(_bytes[1])}.0{oct(last_two)}'.replace('0o', ''))
        print(f'{_bytes[0]}.0{oct(last_three)}'.replace('0o', ''))
