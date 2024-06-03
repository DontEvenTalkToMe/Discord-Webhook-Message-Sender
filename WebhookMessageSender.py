import tkinter as tk
from discordwebhook import Discord

root=tk.Tk()

root.title("Message Input")

root.geometry("400x400")

name_var=tk.StringVar()
user_var=tk.StringVar()
avatar_var=tk.StringVar()
not_var=tk.IntVar()
wurl_var=tk.StringVar()

def submit():

	name=name_var.get()
	user=user_var.get()
	avatar=avatar_var.get()
	net=not_var.get()
	werl=wurl_var.get()

	if user == "":
		user = "Coastellate"
	if avatar == "":
		avatar = "https://i.ibb.co/v14fqZQ/pexels-photo-315998.jpg"
	if net == 0:
		net = 1
	if werl == "":
		werl = "https://discord.com/api/webhooks/1247228090837500088/bPeQ0BTNnLtwjgQrL_9GAg-F_5-QF_eBQAoZFE4-tH5CxiBCGvNqR4dNVDqiJlB5x33v"

	print("The message is : " + name)
	print("The username is : " + user)
	print("The avatar link is : " + avatar)
	print("The amount is : " + str(net))
	print("The webhook URL is : " + werl)
	
	name_var.set("")
	
	discord = Discord(url=werl)
	for i in range(net):
		discord.post(
			content=name,
			username=user,
			avatar_url=avatar,
		)
	


name_label = tk.Label(root, text = 'Message', font=('calibre',10, 'bold'))

name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',14,'normal'))

user_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))

user_entry = tk.Entry(root,textvariable = user_var, font=('calibre',14,'normal'))

avatar_label = tk.Label(root, text = 'Avatar[Put a link]', font=('calibre',10, 'bold'))

avatar_entry = tk.Entry(root,textvariable = avatar_var, font=('calibre',14,'normal'))

not_label = tk.Label(root, text = 'Amount (0 is 1)', font=('calibre',10, 'bold'))

not_entry = tk.Entry(root,textvariable = not_var, font=('calibre',14,'normal'))

wurl_label = tk.Label(root, text = 'Webhook URL', font=('calibre',10, 'bold'))

wurl_entry = tk.Entry(root,textvariable = wurl_var, font=('calibre',14,'normal'))


sub_btn=tk.Button(root,text = 'Submit', command = submit)

name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)

user_label.grid(row=1,column=0)
user_entry.grid(row=1,column=1)

avatar_label.grid(row=2,column=0)
avatar_entry.grid(row=2,column=1)

not_label.grid(row=3,column=0)
not_entry.grid(row=3,column=1)

wurl_label.grid(row=4,column=0)
wurl_entry.grid(row=4,column=1)



sub_btn.grid(row=5,column=0)


root.mainloop()



