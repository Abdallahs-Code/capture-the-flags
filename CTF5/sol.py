import requests

TARGET = 'http://cbc-ctf.westeurope.azurecontainer.io:5000/oracle'
CT_HEX = 'b248f0e8f4e3548b995d2215f54b72bd5d3b211b522b7a5ea25c5763e7425447e440e4d85933807e1385d11cd1959975'

def check_padding(ct_hex):
    try:
        res = requests.post(TARGET, json={"ciphertext_hex": ct_hex}, timeout=5)
        return res.json().get("valid_padding", False)
    except Exception:
        return False

def decrypt_block(prev_block, current_block):
    intermediate = bytearray(16)
    
    for i in range(1, 17):
        target = 16 - i
        for guess in range(256):
            test_prev = bytearray(16)
            
            # Set up the padding bytes we already know
            for j in range(target + 1, 16):
                test_prev[j] = intermediate[j] ^ i
                
            test_prev[target] = guess
            
            if check_padding(test_prev.hex() + current_block.hex()):
                # False positive check for the first byte
                if i == 1:
                    test_prev[target - 1] ^= 1
                    if not check_padding(test_prev.hex() + current_block.hex()):
                        continue
                        
                intermediate[target] = guess ^ i
                break
                
    # XOR intermediate state with the actual previous block to get plaintext
    return bytes(x ^ y for x, y in zip(prev_block, intermediate))

if __name__ == "__main__":
    ct = bytes.fromhex(CT_HEX)
    blocks = [ct[i:i+16] for i in range(0, len(ct), 16)]
    
    plaintext = b""
    for i in range(1, len(blocks)):
        print(f"[*] Decrypting block {i} / {len(blocks)-1}...")
        plaintext += decrypt_block(blocks[i-1], blocks[i])
        
    pad_len = plaintext[-1]
    print(f"\n[+] Flag: {plaintext[:-pad_len].decode()}")