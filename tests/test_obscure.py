import ipaddress
import pytest
from obscure import ObscureIP


class TestObscureIP:
    """Tests using the 203.0.113.0/24 (TEST-NET-3) range."""

    def test_is_ipv4_subclass(self):
        o = ObscureIP("203.0.113.1")
        assert isinstance(o, ipaddress.IPv4Address)

    def test_returns_nonempty_list(self):
        o = ObscureIP("203.0.113.1")
        assert len(o.obscure_ips) > 0

    def test_consistent_count(self):
        o1 = ObscureIP("203.0.113.1")
        o2 = ObscureIP("203.0.113.50")
        assert len(o1.obscure_ips) == len(o2.obscure_ips)

    def test_contains_plain_decimal(self):
        o = ObscureIP("203.0.113.1")
        # full 32-bit integer representation
        expected_int = str(int(ipaddress.IPv4Address("203.0.113.1")))
        assert expected_int in o.obscure_ips

    def test_contains_hex_full(self):
        o = ObscureIP("203.0.113.1")
        expected_hex = hex(int(ipaddress.IPv4Address("203.0.113.1")))
        assert expected_hex in o.obscure_ips

    def test_contains_octal_full(self):
        o = ObscureIP("203.0.113.1")
        val = int(ipaddress.IPv4Address("203.0.113.1"))
        expected_oct = oct(val).replace("o", "")
        assert expected_oct in o.obscure_ips

    def test_contains_dotted_decimal(self):
        o = ObscureIP("203.0.113.1")
        assert "203.0.113.1" in o.obscure_ips

    def test_contains_dotted_hex(self):
        o = ObscureIP("203.0.113.1")
        assert "0xcb.0x0.0x71.0x1" in o.obscure_ips

    def test_contains_dotted_octal(self):
        o = ObscureIP("203.0.113.1")
        assert "0313.00.0161.01" in o.obscure_ips

    def test_mixed_notation(self):
        o = ObscureIP("203.0.113.1")
        # first octet hex, rest decimal
        assert "0xcb.0.113.1" in o.obscure_ips

    def test_two_part_form(self):
        o = ObscureIP("203.0.113.1")
        # first_octet.last_three_bytes_as_int
        assert "203.28929" in o.obscure_ips

    def test_three_part_form(self):
        o = ObscureIP("203.0.113.1")
        # first.second.last_two_as_int
        assert "203.0.28929" in o.obscure_ips

    def test_auto_obscure_false(self):
        o = ObscureIP("203.0.113.10", auto_obscure=False)
        assert o.obscure_ips == []

    def test_manual_obscure_after_init(self):
        o = ObscureIP("203.0.113.10", auto_obscure=False)
        o.obscure()
        assert len(o.obscure_ips) > 0
        assert "203.0.113.10" in o.obscure_ips

    def test_different_addresses_produce_different_results(self):
        o1 = ObscureIP("203.0.113.1")
        o2 = ObscureIP("203.0.113.200")
        assert o1.obscure_ips != o2.obscure_ips

    def test_no_duplicates(self):
        o = ObscureIP("203.0.113.50")
        assert len(o.obscure_ips) == len(set(o.obscure_ips))
