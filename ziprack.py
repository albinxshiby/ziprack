import zipfile

# Ask for location of protected ZIP archive
zip_file = input("Enter the location of the protected ZIP archive: ")

# Create a ZipFile object with the zip_file path
with zipfile.ZipFile(zip_file) as zf:

    # Loop until the user decides to quit
    while True:
        # Ask for location of password list file
        password_list = input("Enter the location of the password list file: ")

        # Open the password list file and read its contents
        with open(password_list, 'r') as pw_file:
            # Loop through each line in the password list file
            for line in pw_file:
                # Strip any whitespace characters from the beginning or end of the line
                password = line.strip()

                try:
                    # Attempt to extract the contents of the ZIP archive using the current password
                    zf.extractall(pwd=password.encode())

                    # If successful, print the cracked password and exit the loop
                    print(f"Cracked password: {password}")
                    break

                except Exception:
                    # If unsuccessful, continue trying other passwords
                    pass

            else:
                # If all passwords have been tried and none worked, print a failure message
                print("Could not crack the password.")

                # Ask the user if they want to retry the password cracking job
                retry = input("Do you want to retry? (y/n)")
                if retry.lower() != 'y':
                    break
