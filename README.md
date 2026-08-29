# SCT_CS_2
🔐 Image Encryption Tool Using Pixel Manipulation
📌 Project Overview
This project is a simple Image Encryption and Decryption Tool developed using Python. The tool encrypts images by manipulating pixel values and rearranging pixel positions, making the original image unreadable without the correct key. The primary goal of this project is to demonstrate the fundamental concepts of cryptography, image processing, and data protection in a practical way.

This project is intended for educational purposes and helps beginners understand how encryption works at a basic level before moving on to advanced cryptographic algorithms such as AES and RSA.

🎯 Objectives
Learn how digital images are represented as pixel data.
Understand the basic principles of encryption and decryption.
Explore pixel manipulation techniques.
Gain hands-on experience with Python image processing libraries.
Demonstrate the concept of symmetric-key encryption.
📖 What is Image Encryption?
Image encryption is the process of converting an image into an unreadable format so that unauthorized users cannot access its contents. The encrypted image appears as random noise or distorted data. Only users possessing the correct decryption key can restore the original image.

Original Image
Readable Image
Encrypted Image
Random Noise
Decrypted Image
Readable Image Restored
Image encryption is commonly used in:

Secure image transmission
Military communication systems
Medical image protection
Cloud storage security
Digital forensics
Confidential document sharing
⚙️ How the Project Works
The encryption process consists of two major steps:

Step 1: Pixel Value Manipulation
Each pixel value is modified using a secret key.

Formula
Encrypted Pixel = (Original Pixel + Key) mod 256
Example
Assume:

Original Pixel = 100
Key = 5
Calculation:

(100 + 5) mod 256 = 105
Result:

Encrypted Pixel = 105
This changes the color information of every pixel in the image.

Step 2: Pixel Position Shuffling
After changing pixel values, the pixels are randomly rearranged.

Example:

Before:

A B C D
After:

C A D B
This destroys the visual structure of the image and makes it appear as random noise.

The shuffle pattern is generated using:

np.random.seed(key)
The same key always produces the same shuffle pattern.

🔓 Decryption Process
The decryption process reverses the encryption steps.

Step 1: Reverse Pixel Shuffling
The original pixel positions are restored.

C A D B
becomes

A B C D
Step 2: Reverse Pixel Manipulation
Formula
Original Pixel = (Encrypted Pixel - Key) mod 256
Example:

Encrypted Pixel = 105
Key = 5

(105 - 5) mod 256 = 100
Result:

Original Pixel = 100
The original image is successfully recovered.

🔑 Why the Key is Important
The key controls:

Pixel value transformation
Pixel shuffling pattern
Without the correct key:

Pixel positions cannot be restored.
Pixel values cannot be recovered.
As a result, the image remains unreadable.

🧠 Concepts Used
1. Cryptography
Cryptography is the science of protecting information by transforming it into a secure format. The project demonstrates:

Encryption
Converting readable data into unreadable data.

Decryption
Converting encrypted data back into readable data.

2. Symmetric Key Encryption
This project uses a symmetric encryption model.

Definition
The same key is used for:

Encryption
Decryption
Example:

Encryption Key = 5
Decryption Key = 5
If different keys are used, the image cannot be recovered.
3. Pixel Manipulation
A digital image consists of pixels. Each pixel stores color information.

For RGB images:

Red   : 0–255
Green : 0–255
Blue  : 0–255
Example:

(255,0,0)
represents a red pixel. The project modifies these pixel values during encryption.
4. Modular Arithmetic
The project uses:

% 256
Why?
Pixel values must remain between:

0 and 255
Example:

250 + 20 = 270
270 mod 256 = 14
This keeps values within the valid pixel range.

5. Randomization
Randomization is used to shuffle pixel positions.

np.random.shuffle()
The random pattern depends on the encryption key. This adds an additional layer of security.

6. NumPy Arrays
Images are converted into NumPy arrays for efficient processing.

Example:

img_array = np.array(img)
Advantages:

Faster computation
Easy pixel manipulation
Efficient memory usage
7. Image Processing
The project uses the Pillow library.

Features Used
Loading images
Converting images to arrays
Saving encrypted images
Saving decrypted images
📚 Python Libraries Used
Pillow (PIL)
Used for image processing.

Installation:

pip install pillow
Functions used:

Image.open()
Image.fromarray()
NumPy
Used for numerical operations and pixel manipulation.

Installation:

pip install numpy
Functions used:

np.array()
np.random.shuffle()
np.arange()
np.mod()
🛠️ Project Structure
Image Encryption Tool
│
├── Image.py
├── Original Image
├── Encrypted Image
├── Decrypted Image
└── README.md
🚀 How to Run the Project
Install Dependencies
pip install pillow numpy
Run the Program
python Image.py
Encrypt an Image
1. Encrypt Image
Enter image path
Enter output file name
Enter encryption key
Decrypt an Image
2. Decrypt Image
Enter encrypted image path
Enter output file name
Enter decryption key
🔒 Security Analysis
Advantages
✔ Demonstrates encryption concepts ✔ Uses both confusion and diffusion ✔ Simple and easy to understand ✔ Good educational cybersecurity project
Limitations
❌ Small key space ❌ Not resistant to brute-force attacks ❌ Not suitable for real-world security ❌ Uses predictable pseudo-random generation ❌ Does not provide cryptographic-level protection
🔮 Future Improvements
Possible enhancements include:

Password-based encryption
AES image encryption
GUI using Tkinter
Drag-and-drop image support
Random key generation
Key file storage
Support for multiple encryption rounds
Histogram analysis
Image integrity verification
Secure cryptographic random number generation
🎓 Learning Outcomes
Through this project, I gained practical experience in:

Python Programming
Image Processing
NumPy Arrays
Pillow Library
Cryptography Fundamentals
Symmetric Encryption
Pixel Manipulation Techniques
Randomization Methods
Encryption and Decryption Workflows
Cybersecurity Concepts
"Understanding how encryption works at a fundamental level is the first step toward building secure systems." 🔐
