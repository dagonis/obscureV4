# obscureV4
Let's obscure some IPv4 addresses

Absolutely requires Python3.6+, confirmed broken on anything older.

## Usage

> python3 obscure $IP

You can use --payload to interpolate the obfuscated IPs into a command using \I as the anchor for where you want the IP to be.

```
python3 obscure $IP --payload "ping -c 4 \I"
```

### Example

```
python3 obscure 216.58.217.206    
3627735502
216.58.217.206
216.58.55758
216.3856846
0xd83ad9ce
0xd8.0x3a.0xd9.0xce
0xd8.58.0xd9.0xce
[...]
```

## Using as a Library

Install the package:

```
pip install -e .
```

Then import and use `ObscureIP` directly:

```python
from obscure import ObscureIP

o = ObscureIP("203.0.113.1")

for ip in o.obscure_ips:
    print(ip)
```

You can also defer generation with `auto_obscure=False`:

```python
o = ObscureIP("203.0.113.1", auto_obscure=False)
# ... do other setup ...
o.obscure()
print(o.obscure_ips)
```
