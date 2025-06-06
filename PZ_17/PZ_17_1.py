import tkinter as tk
from tkinter import ttk

def submit_form():
    result = (
        f"Requester: {requester_var.get()}\n"
        f"Short Name: {shortname_var.get()}\n"
        f"Email: {email_var.get()}\n"
        f"Organization: {org_var.get()}\n"
        f"Country: {country_var.get()}\n"
        f"IPv4 Address: {ip_var.get()}\n"
        f"Hostname: {host_var.get()}\n"
        f"FQDN: {fqdn_var.get()}\n"
        f"Description: {desc_text.get('1.0', tk.END).strip()}"
    )
    print(result)


root = tk.Tk()
root.title("Certificate Self Service Portal")
root.geometry("500x600")


tk.Label(root, text="Certificate Self Service Portal", font=("Arial", 18, "bold")).pack(pady=10)
tk.Label(root, text="Fill out the form to get a certificate.", font=("Arial", 12)).pack()

form_frame = tk.Frame(root)
form_frame.pack(pady=10)


requester_var = tk.StringVar()
shortname_var = tk.StringVar()
email_var = tk.StringVar()
org_var = tk.StringVar()
country_var = tk.StringVar(value="Austria")
ip_var = tk.StringVar()
host_var = tk.StringVar()
fqdn_var = tk.StringVar()


fields = [
    ("Requester", requester_var),
    ("Short Name", shortname_var),
    ("Email", email_var),
    ("Organization", org_var),
    ("IPv4 Address", ip_var),
    ("Hostname", host_var),
    ("FQDN", fqdn_var),
]

for i, (label_text, var) in enumerate(fields):
    tk.Label(form_frame, text=label_text).grid(row=i, column=0, sticky="e", padx=10, pady=5)
    tk.Entry(form_frame, textvariable=var, width=40).grid(row=i, column=1, padx=10, pady=5)


tk.Label(form_frame, text="Country").grid(row=len(fields), column=0, sticky="e", padx=10, pady=5)
ttk.Combobox(form_frame, textvariable=country_var, values=[
    "Austria", "Germany", "USA", "UK", "France", "Other"
], width=37).grid(row=len(fields), column=1, padx=10, pady=5)


tk.Label(form_frame, text="Description").grid(row=len(fields)+1, column=0, sticky="ne", padx=10, pady=5)
desc_text = tk.Text(form_frame, width=30, height=4)
desc_text.grid(row=len(fields)+1, column=1, padx=10, pady=5)

tk.Button(root, text="Submit Form", command=submit_form, bg="#428bca", fg="white", font=("Arial", 12)).pack(pady=20)

root.mainloop()