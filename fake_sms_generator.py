import tkinter as tk
from tkinter import scrolledtext
import random
import string

# List of sample Pakistani names
names = [
    "Ahmed Khan", "Ayesha Malik", "Bilal Shah", "Fatima Noor", "Hassan Ali",
    "Iqra Bibi", "Junaid Akhtar", "Khadija Riaz", "Mohammad Usman", "Nida Farooq",
    "Omar Siddiqui", "Rabia Zafar", "Saad Iqbal", "Tania Rehman", "Umar Cheema",
    "Zainab Arif", "Abdullah Butt", "Erum Javed", "Faisal Qureshi", "Hina Tariq"
]

# Sample SMS messages
messages = [
    "Hey, how's it going? Meet me at the usual spot!",
    "Reminder: Your bill payment is due tomorrow.",
    "Congrats! You've won a free voucher. Call to claim!",
    "Can you send me the notes from today's class?",
    "Let's grab dinner tonight at 7 PM.",
    "Urgent: Please call me back ASAP!",
    "Your order has been shipped. Track it online.",
    "Happy birthday! Hope you have an amazing day!",
    "Meeting rescheduled to 3 PM. Be there!",
    "Just saw your missed call. What's up?",
    "Free entry to the concert this weekend! Interested?",
    "Please confirm your appointment for tomorrow.",
    "New deals available at our store. Visit now!",
    "Can you pick me up from the station at 5?",
    "Your subscription has been renewed successfully."
]

def generate_pakistani_number():
    """Generate a random Pakistani phone number starting with +92."""
    mobile_codes = ["300", "301", "302", "303", "304", "305", "306", "307", "308", "309",
                    "310", "311", "312", "313", "314", "315", "316", "317", "318", "319",
                    "320", "321", "322", "323", "324", "330", "331", "332", "333", "334",
                    "340", "341", "342", "343", "344", "345", "346", "347", "348", "349"]
    code = random.choice(mobile_codes)
    number = ''.join(random.choices(string.digits, k=7))
    return f"+92{code}{number}"

def generate_sms():
    """Generate 50 fake SMS messages and display them."""
    text_area.delete(1.0, tk.END)  # Clear previous content
    for i in range(50):
        sender = random.choice(names)
        number = generate_pakistani_number()
        message = random.choice(messages)
        sms = f"SMS {i+1}:\nFrom: {sender} ({number})\nMessage: {message}\n{'-'*50}\n"
        text_area.insert(tk.END, sms)

# Create the main window
root = tk.Tk()
root.title("Fake SMS Generator (Pakistan)")
root.geometry("600x700")

# Create and pack the title label
title_label = tk.Label(root, text="Generate 50 Fake SMS Messages", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Create and pack the generate button
generate_button = tk.Button(root, text="Generate SMS", font=("Arial", 12), command=generate_sms)
generate_button.pack(pady=10)

# Create and pack the scrolled text area
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=30, font=("Arial", 10))
text_area.pack(padx=10, pady=10)

# Start the main loop
root.mainloop()