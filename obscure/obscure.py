import ipaddress


class ObscureIP(ipaddress.IPv4Address):
    def __init__(self, address, auto_obscure=True):
        super().__init__(address)
        if auto_obscure:
            self.obscure()

    def obscure(self):
        _bytes = int.to_bytes(self._ip, 4, 'big')
        # ints
        first_two = int.from_bytes(_bytes[0:2], 'big')
        first_three = int.from_bytes(_bytes[0:3], 'big')
        all_int = int.from_bytes(_bytes[0:4], 'big')
        middle_two = int.from_bytes(_bytes[1:3], 'big')
        last_two = int.from_bytes(_bytes[-2:], 'big')
        last_three = int.from_bytes(_bytes[-3:], 'big')
        first = _bytes[0]
        second = _bytes[1]
        third = _bytes[2]
        fourth = _bytes[3]
        int_prefixes = [first]
        int_suffixes = [last_two, last_three]
        # hex
        hex_first_two = hex(first_two)
        hex_first_three = hex(first_three)
        hex_all_int = hex(all_int)
        hex_middle_two = hex(middle_two)
        hex_last_two = hex(last_two)
        hex_last_three = hex(last_three)
        hex_first = hex(_bytes[0])
        hex_second = hex(_bytes[1])
        hex_third = hex(_bytes[2])
        hex_fourth = hex(_bytes[3])
        hex_prefixes = [hex_first, hex_first_two, hex_first_three]
        hex_suffixes = [hex_last_two, hex_last_three]
        #octal
        oct_first_two = oct(first_two).replace('o', '')
        oct_first_three = oct(first_three).replace('o', '')
        oct_all_int = oct(all_int).replace('o', '')
        oct_middle_two = oct(middle_two).replace('o', '')
        oct_last_two = oct(last_two).replace('o', '')
        oct_last_three = oct(last_three).replace('o', '')
        oct_first = oct(_bytes[0]).replace('o', '')
        oct_second = oct(_bytes[1]).replace('o', '')
        oct_third = oct(_bytes[2]).replace('o', '')
        oct_fourth = oct(_bytes[3]).replace('o', '')
        oct_prefixes = [oct_first, oct_first_two, oct_first_three]
        oct_suffixes = [oct_last_two, oct_last_three]
        # Collections to make this easier
        single_byte_prefixes = [first, hex_first, oct_first]
        two_byte_prefixes = [first_two, hex_first_two, oct_first_two]
        three_byte_prefixes = [first_three, hex_first_three, oct_first_three]
        single_byte_suffixes = [fourth, hex_fourth, oct_fourth]
        two_byte_suffixes = [last_two, hex_last_two, oct_last_two]
        three_byte_suffixes = [last_three, hex_last_three, oct_last_three]
        second_bytes = [second, hex_second, oct_second]
        third_bytes = [third, hex_third, oct_third]
        fourth_bytes = [fourth, hex_fourth, oct_fourth]
        #Let's start printing
        print(all_int)
        print(hex(all_int))
        print(oct(all_int).replace('o', ''))
        for single_byte_prefix in single_byte_prefixes:
            for three_byte_suffix in three_byte_suffixes:
                print(f'{single_byte_prefix}.{three_byte_suffix}')
        for single_byte_prefix in single_byte_prefixes:
            for second_byte in second_bytes:
                for two_byte_suffix in two_byte_suffixes:
                    print(f'{single_byte_prefix}.{second_byte}.{two_byte_suffix}')
        for single_byte_prefix in single_byte_prefixes:
            for second_byte in second_bytes:
                for third_byte in third_bytes:
                    for fourth_byte in fourth_bytes:
                        print(f'{single_byte_prefix}.{second_byte}.{third_byte}.{fourth_byte}')