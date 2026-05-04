# 🏁 CTF Solutions – CMPS426

This repository contains solutions for the **Capture The Flag (CTF)** challenges from the CMPS426 – Security of Computer Systems and Networks course 

---

## 📘 Overview

This project includes solutions to multiple CTF challenges covering different areas of cybersecurity, including:

- Network traffic analysis  
- Image processing & steganography  
- Bit manipulation  
- Cryptographic attacks  
- RSA vulnerabilities  

Each challenge required analyzing a different type of data and applying appropriate techniques to recover hidden flags.

---

## 🧩 Challenges & Solutions

### 🔍 CTF1 – Packet Analysis

**Objective:** Recover a flag hidden inside a network capture file.

**Approach:**
- Filtered traffic on TCP port `4444`
- Used *Follow TCP Stream* to reconstruct fragmented packets
- Identified a Base64-encoded payload inside custom markers
- Decoded the payload to retrieve the flag

**Flag:**
```
CMPN{pc4p_hidd3n_in_l3gi7_7r4ffic}
```

---

### 🖼️ CTF2 – Image Manipulation

**Objective:** Extract hidden data from two noisy images.

**Approach:**
- Compared corresponding pixels between the two images
- Applied operations such as:
  - Addition  
  - Subtraction  
  - Averaging  
- These operations revealed the hidden content

**Flag:**
```
CMPN{im4g3s-4s_k3y$}
```

---

### 🔢 CTF3 – Bit Shifting

**Objective:** Recover text from shifted numeric values.

**Approach:**
- Observed that all numbers were even → LSB = 0  
- Concluded values were likely **left-shifted**
- Applied a **right shift (>> 1)** to reverse the operation

**Flag:**
```
CMPN{bi7_shif7ing_is_w34k}
```

---

### 🕵️ CTF4 – Steganography (LSB)

**Objective:** Extract hidden data from an image.

**Approach:**
- Used **LSB (Least Significant Bit) extraction**
- Steps:
  - Read image pixels  
  - Extract LSB from each pixel  
  - Group bits into bytes  
  - Convert to ASCII text  
  - Search for flag pattern  

**Flag:**
```
CMPN{Hidd3n_in_pl4in_sigh7}
```

---

### 🔓 CTF5 – CBC Padding Oracle Attack

**Objective:** Decrypt AES-CBC ciphertext without the key.

**Approach:**
- Observed server response indicating valid/invalid padding  
- Used a **Padding Oracle Attack**:
  - Modified ciphertext byte-by-byte  
  - Used server feedback to deduce plaintext  
- Reconstructed full plaintext using XOR operations

**Flag:**
```
CMPN{cbc_p4dding_0r4cl3}
```

---

### 🔐 CTF6 – RSA Key Recovery

**Objective:** Decrypt RSA ciphertext with weak key generation.

**Approach:**
- Attempted **Fermat’s factorization** (since primes were said to be close)  
- Failed after long runtime → primes not close enough  
- Used `factorint` (SymPy), which applies:
  - Pollard’s Rho  
  - Other optimized factorization methods  
- Recovered prime factors → computed private key → decrypted message  

**Flag:**
```
CMPN{f4c70r_m3}
```

---

## 🧠 Key Learnings

- Real-world protocols can leak sensitive data (CTF1)  
- Simple image operations can reveal hidden data (CTF2)  
- Weak transformations like bit shifting are reversible (CTF3)  
- LSB steganography is easy to exploit (CTF4)  
- Improper error handling enables powerful attacks (CTF5)  
- Weak RSA key generation breaks security (CTF6)  

---

## 🛠️ Tools & Techniques Used

- Wireshark (packet analysis)  
- Python (automation & scripting)  
- OpenCV / NumPy (image processing)  
- SymPy (number factorization)  
- Custom scripts for cryptographic attacks  

---

## 📌 Notes

- All solutions are for educational purposes  
- Demonstrates practical weaknesses in poorly implemented systems  

---

## 👨‍💻 Contributors
- Abdullah Ahmed  
- Ali Alaa Abdelaziz Niazi 
- Ahmed Mohamed Ahmed 
- Omar Ahmed Reda
