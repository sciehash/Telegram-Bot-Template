# WELCOMING USER

rname = []
ctry = []
uname = []
mail = []


def UserData():
    # Let user input their data
    realname = input(str("""Welcome! I am SvetiBot. Before we get started,
we need to know each other first. What's your name? (example: John Adams)
"""))
    country = input(str("""Where are you from? (example: United States of America)
"""))
    username = input(str("""What username you'd like to use? (example: jadams75)
"""))
    email = input(str("""Please enter your email: (example: jadams@emailprovider.com)
"""))

    # Let user review their data before being entered to database
    print("")
    print("A plus! Let's review your data")
    print("")
    print(f"Name: {realname}")
    print(f"Country: {country}")
    print(f"Username: {username}")
    print(f"E-mail: {email}")
    print("")
    confirm = input(str("Are these correct? y - YES n - NO "))

    if confirm == "y":
        print("""Welcome to our community! I hope you'll have a good time, 
and whenever you need help, SvetiBot will be here for you <3

Come back later for the giveaway announcement, and press the 'Announcement' button.""")
    else:
        print("Okay, let's try again.")
        UserData()

    #Enter Input-ed data to list, to be used later
    rname.append(realname)
    ctry.append(country)
    uname.append(username)
    mail.append(email)


def MyAccount():
    print("Your Account:")
    print("")
    print(f"Name: {rname}")
    print(f"Country: {ctry}")
    print(f"Username: {uname}")
    print(f"E-mail: {mail}")

UserData()







